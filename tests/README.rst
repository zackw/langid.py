Test Corpus
-----------

This directory contains labeled examples (one per file) of each of the
97 languages recognized by the default model, plus <> more languages
which are *not* recognized by the default model.  Each example is
roughly 500 words.

All were taken from online sources which are either definitively
public domain, or are otherwise safe to redistribute (though possibly
not modify); each file has a four-line comment at the beginning,
naming the author, title, language, and URL of the source.  The ISO
639 code for the language (-1 if available, else -2 or -3) is also
embedded in the filename, followed by a period.  Languages not
recognized by the default model have ``(NR)`` after the language name
in the file, and an underscore in between the ISO code and the period.

Languages recognized by the default model and covered by the test suite
-----------------------------------------------------------------------

== ===========================
af Afrikaans
am Amharic
an Aragonese
ar Arabic
as Assamese
az Azerbaijani (Latin script)
az Azerbaijani (Arabic script)
be Belarusian
bg Bulgarian
bn Bengali
br Breton
bs Bosnian
ca Catalan
cs Czech
cy Welsh
da Danish
de German
dz Dzongkha
el Greek
en English
eo Esperanto
es Spanish
et Estonian
eu Basque
fa Farsi
fi Finnish
fo Faroese
fr French
ga Irish Gaelic
gl Galician
gu Gujarati
he Hebrew
hi Hindi
hr Croatian
ht Haitian
hu Hungarian
hy Armenian
id Indonesian
is Icelandic
it Italian
ja Japanese
jv Javanese
ka Georgian
kk Kazakh (Cyrillic)
kk Kazakh (Arabic)
kk Kazakh (Latin)
km Khmer
kn Kannada
ko Korean
ku Kurdish
ky Kyrgyz
la Latin
lb Luxembourgish
lo Lao
lt Lithuanian
lv Latvian
mg Malagasy
mk Macedonian
ml Malayalam
mn Mongolian (Cyrillic)
mr Marathi
ms Malay
mt Maltese
nb Norwegian (Bokmål)
ne Nepali
nl Dutch
nn Norwegian (Nynorsk)
no Norwegian (macro)
oc Occitan
or Oriya
pa Punjabi
pl Polish
ps Pashto
pt Portuguese
ro Romanian
ru Russian
rw Kinyarwanda
se Northern Sami
si Sinhala
sk Slovak
sl Slovenian
sq Albanian
sr Serbian
sv Swedish
sw Swahili
ta Tamil
te Telugu
th Thai
tl Tagalog
tr Turkish
ug Uyghur
uk Ukrainian
ur Urdu
vi Vietnamese
vo Volapük
wa Walloon
zh Chinese
== ===========================

Languages covered by the default model, but not yet the test suite
------------------------------------------------------------------

== ===========================
qu Quechua
xh Xhosa
zu Zulu
== ===========================

Languages in the test suite but not recognized by the default model
-------------------------------------------------------------------

=== ===========================
ada Adangme
arn Mapudungun
ast Asturian
arp Arapaho
rmq Caló
fy  West? Frisian
fur Friulian
gd  Scottish Gaelic
kld Kamilaroi
ceb Visayan / Cebuano
ilo Ilokano
ia  Interlingua
iu  Inuktitut
csb Kashubian
kha Khasi
lad Ladino
mi  Maori
myn Mayan
xmm Manado Malay
nah Nahuatl
nap Neapolitan
oj  Ojibwe
=== ===========================

Other languages with more than 7.4 million native speakers
----------------------------------------------------------

according to `Wikipedia's list
<https://en.wikipedia.org/wiki/List_of_languages_by_number_of_native_speakers>`__,
and treating all varieties of Chinese as one language.

=== ===========================
su  Sundanese
ha  Hausa
my  Burmese
bho Bhojpuri
yo  Yoruba
mai Maithili
uz  Uzbek
sd  Sindhi
ff  Fula
om  Oromo
ig  Igbo
awa Awadhi
skr Saraiki
ctg Chittagonian
za  Zhuang
mad Madurese
so  Somali
mwr Marwari
mag Magahi
bgc Haryanvi
hne Chhatisgarhi
ny  Chewa
dcc Dakhini
ak  Akan
syl Sylheti
dhd Dhundari
rn  Kirundi
hmv Hmong
sn  Shona
hil Hiligaynon
mos Mossi
bal Balochi
kok Konkani
=== ============================
