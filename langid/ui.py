"""langid.py - Language Identifier by Marco Lui April 2011 - UI code

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

# Defaults for inbuilt server
HOST = None  # Leave as None for auto-detect
PORT = 9008
FORCE_WSGIREF = False

import json
import optparse
from wsgiref.util import shift_path_info
from urllib.parse import parse_qs

import logging
logger = logging.getLogger(__name__)

from .identifier import LanguageIdentifier

# Based on http://www.ubacoda.com/index.php?p=8
query_form = """
<html>
    <head>
        <meta http-equiv="Content-type" content="text/html; charset=utf-8">
        <title>Language Identifier</title>
        <script src="//ajax.googleapis.com/ajax/libs/jquery/1.7.2/jquery.min.js" type="text/javascript"></script>
        <script type="text/javascript" charset="utf-8">
            $(document).ready(function() {{
                $("#typerArea").keyup(displayType);
                function displayType(){{
                    var contents = $("#typerArea").val();
                    if (contents.length != 0) {{
                        $.post(
                            "/rank",
                            {{q:contents}},
                            function(data){{
                                for(i=0;i<5;i++) {{
                                    $("#lang"+i).html(data.responseData[i][0]);
                                    $("#conf"+i).html(data.responseData[i][1]);
                                }}
                                $("#rankTable").show();
                            }},
                            "json"
                        );
                    }}
                    else {{
                        $("#rankTable").hide();
                    }}
                }}
                $("#manualSubmit").remove();
                $("#rankTable").hide();
            }});
        </script>
    </head>
    <body>
        <form method=post>
            <center><table>
                <tr>
                    <td>
                        <textarea name="q" id="typerArea" cols=40 rows=6></textarea></br>
                    </td>
                </tr>
                <tr>
                    <td>
                        <table id="rankTable">
                            <tr>
                                <td id="lang0">
                                    <p>Unable to load jQuery, live update disabled.</p>
                                </td><td id="conf0"/>
                            </tr>
                            <tr><td id="lang1"/><td id="conf1"></tr>
                            <tr><td id="lang2"/><td id="conf2"></tr>
                            <tr><td id="lang3"/><td id="conf3"></tr>
                            <tr><td id="lang4"/><td id="conf4"></tr>
                        </table>
                        <input type=submit id="manualSubmit" value="submit">
                    </td>
                </tr>
            </table></center>
        </form>

    </body>
</html>
"""


def application(environ, start_response):
    """
    WSGI-compatible langid web service.
    """
    try:
        path = shift_path_info(environ)
    except IndexError:
        # Catch shift_path_info's failure to handle empty paths properly
        path = ''

    if path == 'detect' or path == 'rank':
        data = None

        # Extract the data component from different access methods
        if environ['REQUEST_METHOD'] == 'PUT':
            data = environ['wsgi.input'].read(int(environ['CONTENT_LENGTH']))
        elif environ['REQUEST_METHOD'] == 'GET':
            try:
                data = parse_qs(environ['QUERY_STRING'])['q'][0]
            except KeyError:
                # No query, provide a null response.
                status = '200 OK' # HTTP Status
                response = {
                    'responseData': None,
                    'responseStatus': 200,
                    'responseDetails': None,
                }
        elif environ['REQUEST_METHOD'] == 'POST':
            input_string = environ['wsgi.input'].read(int(environ['CONTENT_LENGTH']))
            try:
                data = parse_qs(input_string)['q'][0]
            except KeyError:
                # No key 'q', process the whole input instead
                data = input_string
        else:
            # Unsupported method
            status = '405 Method Not Allowed'  # HTTP Status
            response = {
                'responseData': None,
                'responseStatus': 405,
                'responseDetails': '%s not allowed' % environ['REQUEST_METHOD']
            }

        if data is not None:
            if path == 'detect':
                pred, conf = classify(data)
                responseData = {'language': pred, 'confidence': conf}
            elif path == 'rank':
                responseData = rank(data)

            status = '200 OK' # HTTP Status
            response = {
                'responseData': responseData,
                'responseStatus': 200,
                'responseDetails': None,
            }
    elif path == 'demo':
        status = '200 OK'  # HTTP Status
        headers = [('Content-type', 'text/html; charset=utf-8')] # HTTP Headers
        start_response(status, headers)
        return [query_form.format(**environ)]

    else:
        # Incorrect URL
        status = '404 Not Found'
        response = {'responseData': None, 'responseStatus': 404, 'responseDetails': 'Not found'}

    headers = [('Content-type', 'text/javascript; charset=utf-8')]  # HTTP Headers
    start_response(status, headers)
    return [json.dumps(response)]

def main():

    parser = optparse.OptionParser()
    parser.add_option('-s', '--serve',
                      action='store_true', default=False, dest='serve', help='launch web service')
    parser.add_option('--host',
                      default=HOST, dest='host', help='host/ip to bind to')
    parser.add_option('--port',
                      default=PORT, dest='port', help='port to listen on')
    parser.add_option('-v',
                      action='count', dest='verbosity', help='increase verbosity (repeat for greater effect)')
    parser.add_option('-m',
                      dest='model', help='load model from file')
    parser.add_option('-l', '--langs',
                      dest='langs', help='comma-separated set of target ISO639 language codes (e.g en,de)')
    parser.add_option('-r', '--remote',
                      action="store_true", default=False, help='auto-detect IP address for remote access')
    parser.add_option('-b', '--batch',
                      action="store_true", default=False, help='specify a list of files on the command line')
    parser.add_option('--demo',
                      action="store_true", default=False, help='launch an in-browser demo application')
    parser.add_option('-d', '--dist',
                      action='store_true', default=False, help='show full distribution over languages')
    parser.add_option('-u', '--url',
                      help='langid of URL')
    parser.add_option('--line',
                      action="store_true", default=False, help='process pipes line-by-line rather than as a document')
    parser.add_option('-n', '--normalize',
                      action='store_true', default=False, help='normalize confidence scores to probability values')
    options, args = parser.parse_args()

    if options.verbosity:
        logging.basicConfig(level=max((5-options.verbosity)*10, 0))
    else:
        logging.basicConfig()

    if options.batch and options.serve:
        parser.error("cannot specify both batch and serve at the same time")

    # unpack a model
    identifier = None
    if options.model:
        try:
            identifier = LanguageIdentifier.from_modelpath(
                options.model, norm_probs=options.normalize)
            logger.info("Using external model: %s", options.model)
        except IOError as e:
            logger.warning("Failed to load %s: %s" % (options.model,e))

    if identifier is None:
        identifier = LanguageIdentifier.from_model(norm_probs=options.normalize)
        logger.info("Using internal model")

    if options.langs:
        langs = options.langs.split(",")
        identifier.set_languages(langs)

    def _process(text):
        """
        Set up a local function to do output, configured according to our settings.
        """
        if options.dist:
            payload = identifier.rank(text)
        else:
            payload = identifier.classify(text)

        return payload


    if options.url:
        import urllib.request, urllib.error, urllib.parse
        import contextlib
        with contextlib.closing(urllib.request.urlopen(options.url)) as url:
            text = url.read()
            output = _process(text)
            print(options.url, len(text), output)

    elif options.serve or options.demo:
        # from http://stackoverflow.com/questions/166506/finding-local-ip-addresses-in-python
        if options.remote and options.host is None:
            # resolve the external ip address
            import socket
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect(("google.com", 80))
            hostname = s.getsockname()[0]
        elif options.host is None:
            # resolve the local hostname
            import socket
            hostname = socket.gethostbyname(socket.gethostname())
        else:
            hostname = options.host

        if options.demo:
            import webbrowser
            webbrowser.open('http://{0}:{1}/demo'.format(hostname, options.port))
        try:
            if FORCE_WSGIREF:
                raise ImportError
            # Use fapws3 if available
            import fapws._evwsgi as evwsgi
            from fapws import base
            evwsgi.start(hostname, str(options.port))
            evwsgi.set_base_module(base)
            evwsgi.wsgi_cb(('', application))
            evwsgi.set_debug(0)
            evwsgi.run()
        except ImportError:
            print("Listening on %s:%d" % (hostname, int(options.port)))
            print("Press Ctrl+C to exit")
            from wsgiref.simple_server import make_server
            httpd = make_server(hostname, int(options.port), application)
            try:
                httpd.serve_forever()
            except KeyboardInterrupt:
                pass
    elif options.batch:
        # Start in batch mode - interpret input as paths rather than content
        # to classify.
        import sys
        import os
        import csv
        import multiprocessing as mp

        def generate_paths():
            for line in sys.stdin:
                path = line.strip()
                if path:
                    if os.path.isfile(path):
                        yield path
                    else:
                        # No such path
                        pass

        writer = csv.writer(sys.stdout)
        pool = mp.Pool()
        if options.dist:
            writer.writerow(['path']+nb_classes)
            for path, ranking in pool.imap_unordered(rank_path, generate_paths()):
                ranking = dict(ranking)
                row = [path] + [ranking[c] for c in nb_classes]
                writer.writerow(row)
        else:
            for path, (lang,conf) in pool.imap_unordered(cl_path, generate_paths()):
                writer.writerow((path, lang, conf))
    else:
        import sys
        if sys.stdin.isatty():
            # Interactive mode
            while True:
                try:
                    print(">>>", end=' ')
                    text = input()
                except Exception:
                    break
                print(_process(text))
        else:
            # Redirected
            if options.line:
                for line in sys.stdin.readlines():
                    print(_process(line))
            else:
                print(_process(sys.stdin.read()))
