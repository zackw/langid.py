"""langid.py - Language Identifier by Marco Lui April 2011 - Core classifier

Based on research by Marco Lui and Tim Baldwin.

Copyright 2011 Marco Lui <saffsd@gmail.com>. All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions
are met:

  1. Redistributions of source code must retain the above copyright
     notice, this list of conditions and the following disclaimer.

  2. Redistributions in binary form must reproduce the above copyright
     notice, this list of conditions and the following disclaimer in
     the documentation and/or other materials provided with the
     distribution.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDER ``AS IS'' AND ANY
EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR
PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR
CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR
PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF
LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

The views and conclusions contained in the software and documentation
are those of the authors and should not be interpreted as representing
official policies, either expressed or implied, of the copyright
holder.

"""

# NORM_PROBS can be set to False for a small speed increase. It does not
# affect the relative ordering of the predicted classes.
NORM_PROBS = True  # Normalize output probabilities.

__all__ = ["set_languages",
           "classify",
           "rank",
           "cl_path",
           "rank_path",
           "load_model",
           "LanguageIdentifier"]

import collections
import numpy as np

import logging
logger = logging.getLogger(__name__)


# Utility: decompress and unpickle a byte blob which may or may not
# have been base64-ed and which might be any of gzip, bzip2, or
# lzma-compressed, or even just a plain old pickle.
def unpack_model(model):
    def un_base64(blob):
        import base64
        return base64.b64decode(blob)
    def un_gzip(blob):
        import zlib
        # The magic argument 31 means "decompress a gzip-format blob".
        return zlib.decompress(blob, 31)
    def un_bzip2(blob):
        import bz2
        return bz2.decompress(blob)
    def un_lzma(blob):
        import lzma
        return lzma.decompress(blob)
    def un_pickle(blob):
        # cPickle merged into pickle in py3
        try:
            import cPickle as pickle
        except ImportError:
            import pickle
        return pickle.loads(blob)

    magic_dict = {
        # all four pickle pseudo-magics (as of Python 3.4)
        # for protocol 0 and 1, we rely on the fact that we know the
        # datum inside the pickle is a tuple, and therefore will start
        # with a MARK opcode.
        b"(":        [un_pickle],
        b"\x80\x02": [un_pickle],
        b"\x80\x03": [un_pickle],
        b"\x80\x04": [un_pickle],

        # the three supported compression formats
        b"\x1f\x8b\x08":             [un_gzip,  un_pickle],
        b"\x42\x5a\x68":             [un_bzip2, un_pickle],
        b"\xfd\x37\x7a\x58\x5a\x00": [un_lzma,  un_pickle],

        # any of the above wrapped in base64
        b"K":        [un_base64, un_pickle],
        b"gA":       [un_base64, un_pickle],
        b"H4sI":     [un_base64, un_gzip,  un_pickle],
        b"Qlpo":     [un_base64, un_bzip2, un_pickle],
        b"/Td6WFoA": [un_base64, un_lzma,  un_pickle],
    }

    for magic, pipeline in magic_dict.items():
        if model.startswith(magic):
            for fn in pipeline:
                model = fn(model)
            return model

    raise RuntimeError("model format not recognized (first six bytes: %s)"
                       % base64.b16encode(model[:6]).decode("ascii").lower())


# Convenience methods defined below will initialize this when first called.
identifier = None
def load_model(path=None):
    """
    Convenience method to set the global identifier using a model at a
    specified path.

    @param path - path to model, or None for the bundled default
    """
    logger.info('initializing global identifier')
    global identifier

    identifier = LanguageIdentifier.from_modelpath(path)


def set_languages(langs=None):
    """
    Set the language set used by the global identifier.

    @param langs a list of language codes
    """
    global identifier
    if identifier is None:
        load_model()

    return identifier.set_languages(langs)


def classify(instance):
    """
    Convenience method using a global identifier instance with the default
    model included in langid.py. Identifies the language that a string is
    written in.

    @param   instance  a text string. Unicode strings will automatically
             be utf8-encoded
    @returns a tuple of the most likely language and the confidence score
    """
    global identifier
    if identifier is None:
        load_model()

    return identifier.classify(instance)


def rank(instance):
    """
    Convenience method using a global identifier instance with the
    default model included in langid.py. Ranks all the languages in
    the model according to the likelihood that the string is written
    in each language.

    @param   instance  a text string. Unicode strings will automatically
             be utf8-encoded
    @returns a list of tuples language and the confidence score, in
             descending order
    """
    global identifier
    if identifier is None:
        load_model()

    return identifier.rank(instance)


def cl_path(path):
    """
    Convenience method using a global identifier instance with the
    default model included in langid.py. Identifies the language that
    the file at `path` is written in.

    @param   path  path to file
    @returns a tuple of the most likely language and the confidence score

    """
    global identifier
    if identifier is None:
        load_model()

    return identifier.cl_path(path)


def rank_path(path):
    """
    Convenience method using a global identifier instance with the
    default model included in langid.py. Ranks all the languages in
    the model according to the likelihood that the file at `path` is
    written in each language.

    @param   path   path to file

    @returns a list of tuples language and the confidence score,
             in descending order
    """
    global identifier
    if identifier is None:
        load_model()

    return identifier.rank_path(path)


class LanguageIdentifier(object):
    """
    This class implements the actual language identifier.
    """

    @classmethod
    def from_model(cls, model=None, *args, **kwargs):
        if model is None:
            import pkgutil
            model = pkgutil.get_data("langid", "model.bz2")

        nb_ptc, nb_pc, nb_classes, tk_nextmove, tk_output = unpack_model(model)
        return cls(nb_ptc, nb_pc, nb_classes, tk_nextmove, tk_output,
                   *args, **kwargs)

    @classmethod
    def from_modelpath(cls, path, *args, **kwargs):
        with open(path, "rb") as f:
            return cls.from_model(f.read(), *args, **kwargs)

    def __init__(self, nb_ptc, nb_pc, nb_classes, tk_nextmove, tk_output,
                 norm_probs=NORM_PROBS):

        nb_numfeats = len(nb_ptc) / len(nb_pc)

        # reconstruct pc and ptc
        nb_pc = np.array(nb_pc)
        nb_ptc = np.array(nb_ptc).reshape(nb_numfeats, len(nb_pc))

        self.nb_ptc = nb_ptc
        self.nb_pc = nb_pc
        self.nb_numfeats = nb_numfeats
        self.nb_classes = nb_classes
        self.tk_nextmove = tk_nextmove
        self.tk_output = tk_output
        self.do_norm_probs = norm_probs

        # Maintain a reference to the full model, in case we change our
        # language set multiple times.
        self.__full_model = nb_ptc, nb_pc, nb_classes

    def set_languages(self, langs=None):
        logger.debug("restricting languages to: %s", langs)

        # Unpack the full original model. This is needed in case the
        # language set has been previously trimmed, and the new set is
        # not a subset of the current set.
        nb_ptc, nb_pc, nb_classes = self.__full_model

        if langs is None:
            self.nb_classes = nb_classes
            self.nb_ptc = nb_ptc
            self.nb_pc = nb_pc

        else:
            # We were passed a restricted set of languages. Trim the
            # arrays accordingly to speed up processing.
            for lang in langs:
                if lang not in nb_classes:
                    raise ValueError("Unknown language code %s" % lang)

            subset_mask = np.fromiter((l in langs for l in nb_classes),
                                      dtype=bool)
            self.nb_classes = [c for c in nb_classes if c in langs]
            self.nb_ptc = nb_ptc[:, subset_mask]
            self.nb_pc = nb_pc[subset_mask]

    def instance2fv(self, text):
        """
        Map an instance into the feature space of the trained model.
        """
        if isinstance(text, str):
            text = text.encode('utf8')

        arr = np.zeros((self.nb_numfeats,), dtype='uint32')

        # Count the number of times we enter each state
        state = 0
        statecount = collections.defaultdict(int)
        for letter in text:
            state = self.tk_nextmove[(state << 8) + letter]
            statecount[state] += 1

        # Update all the productions corresponding to the state
        for state in statecount:
            for index in self.tk_output.get(state, []):
                arr[index] += statecount[state]

        return arr

    def nb_classprobs(self, fv):
        # compute the partial log-probability of the document given each class
        pdc = np.dot(fv, self.nb_ptc)
        # compute the partial log-probability of the document in each class
        pd = pdc + self.nb_pc
        return pd


    def norm_probs(self, pd):
        """
        Renormalize log-probs into a proper distribution (sum 1)
        The technique for dealing with underflow is described in
        http://jblevins.org/log/log-sum-exp
        """
        if self.do_norm_probs:
            # Ignore overflow when computing the exponential. Large values
            # in the exp produce a result of inf, which does not affect
            # the correctness of the calculation (as 1/x->0 as x->inf).
            # On Linux this does not actually trigger a warning, but on
            # Windows this causes a RuntimeWarning, so we explicitly
            # suppress it.
            with np.errstate(over='ignore'):
                pd = (1/np.exp(pd[None, :] - pd[:, None]).sum(1))
        return pd

    def classify(self, text):
        """
        Classify an instance.
        """
        fv = self.instance2fv(text)
        probs = self.norm_probs(self.nb_classprobs(fv))
        cl = np.argmax(probs)
        conf = float(probs[cl])
        pred = str(self.nb_classes[cl])
        return pred, conf

    def rank(self, text):
        """
        Return a list of languages in order of likelihood.
        """
        fv = self.instance2fv(text)
        probs = self.norm_probs(self.nb_classprobs(fv))
        return [(str(k),float(v))
                for (v,k) in sorted(zip(probs, self.nb_classes), reverse=True)]

    def cl_path(self, path):
        """
        Classify a file at a given path
        """
        with open(path) as f:
            retval = self.classify(f.read())
        return path, retval

    def rank_path(self, path):
        """
        Class ranking for a file at a given path
        """
        with open(path) as f:
            retval = self.rank(f.read())
        return path, retval
