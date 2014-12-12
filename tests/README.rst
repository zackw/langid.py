Test Corpus
-----------

This directory contains labeled examples (one per file) of each of the
97 languages recognized by the default model, plus [TBD] more
languages which are *not* recognized by the default model.  Each
example is roughly 500 words.

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

==  ===========================
af  `Afrikaans <https://en.wikipedia.org/wiki/Afrikaans>`__
am  `Amharic <https://en.wikipedia.org/wiki/Amharic>`__
an  `Aragonese <https://en.wikipedia.org/wiki/Aragonese_language>`__
ar  `Arabic <https://en.wikipedia.org/wiki/Arabic_language>`__
as  `Assamese <https://en.wikipedia.org/wiki/Assamese_language>`__
az  `Azerbaijani <https://en.wikipedia.org/wiki/Azerbaijani_language>`__ (Arabic, Latin)
be  `Belarusian <https://en.wikipedia.org/wiki/Belarusian_language>`__
bg  `Bulgarian <https://en.wikipedia.org/wiki/Bulgarian_language>`__
bn  `Bengali <https://en.wikipedia.org/wiki/Bengali_language>`__
br  `Breton <https://en.wikipedia.org/wiki/Breton_language>`__
bs  `Bosnian <https://en.wikipedia.org/wiki/Bosnian_language>`__
ca  `Catalan <https://en.wikipedia.org/wiki/Catalan_language>`__
cs  `Czech <https://en.wikipedia.org/wiki/Czech_language>`__
cy  `Welsh <https://en.wikipedia.org/wiki/Welsh_language>`__
da  `Danish <https://en.wikipedia.org/wiki/Danish_language>`__
de  `German <https://en.wikipedia.org/wiki/German_language>`__
dz  `Dzongkha <https://en.wikipedia.org/wiki/Dzongkha>`__
el  `Greek <https://en.wikipedia.org/wiki/Greek_language>`__
en  `English <https://en.wikipedia.org/wiki/English_language>`__
eo  `Esperanto <https://en.wikipedia.org/wiki/Esperanto>`__
es  `Spanish <https://en.wikipedia.org/wiki/Spanish_language>`__
et  `Estonian <https://en.wikipedia.org/wiki/Estonian_language>`__
eu  `Basque <https://en.wikipedia.org/wiki/Basque_language>`__
fa  `Persian <https://en.wikipedia.org/wiki/Persian_language>`__
fi  `Finnish <https://en.wikipedia.org/wiki/Finnish_language>`__
fo  `Faroese <https://en.wikipedia.org/wiki/Faroese_language>`__
fr  `French <https://en.wikipedia.org/wiki/French_language>`__
ga  `Irish <https://en.wikipedia.org/wiki/Irish_language>`__
gl  `Galician <https://en.wikipedia.org/wiki/Galician_language>`__
gu  `Gujarati <https://en.wikipedia.org/wiki/Gujarati_language>`__
he  `Hebrew <https://en.wikipedia.org/wiki/Hebrew_language>`__
hi  `Hindi <https://en.wikipedia.org/wiki/Hindi>`__
hr  `Croatian <https://en.wikipedia.org/wiki/Croatian_language>`__
ht  `Haitian <https://en.wikipedia.org/wiki/Haitian_Creole>`__
hu  `Hungarian <https://en.wikipedia.org/wiki/Hungarian_language>`__
hy  `Armenian <https://en.wikipedia.org/wiki/Armenian_language>`__
id  `Indonesian <https://en.wikipedia.org/wiki/Indonesian_language>`__
is  `Icelandic <https://en.wikipedia.org/wiki/Icelandic_language>`__
it  `Italian <https://en.wikipedia.org/wiki/Italian_language>`__
ja  `Japanese <https://en.wikipedia.org/wiki/Japanese_language>`__
jv  `Javanese <https://en.wikipedia.org/wiki/Javanese_language>`__
ka  `Georgian <https://en.wikipedia.org/wiki/Georgian_language>`__
kk  `Kazakh <https://en.wikipedia.org/wiki/Kazakh_language>`__ (Cyrillic, Arabic, Latin)
km  `Khmer <https://en.wikipedia.org/wiki/Khmer_language>`__
kn  `Kannada <https://en.wikipedia.org/wiki/Kannada_language>`__
ko  `Korean <https://en.wikipedia.org/wiki/Korean_language>`__
ku  `Kurdish <https://en.wikipedia.org/wiki/Kurdish_languages>`__
ky  `Kyrgyz <https://en.wikipedia.org/wiki/Kyrgyz_language>`__
la  `Latin <https://en.wikipedia.org/wiki/Latin>`__
lb  `Luxembourgish <https://en.wikipedia.org/wiki/Luxembourgish_language>`__
lo  `Lao <https://en.wikipedia.org/wiki/Lao_language>`__
lt  `Lithuanian <https://en.wikipedia.org/wiki/Lithuanian_language>`__
lv  `Latvian <https://en.wikipedia.org/wiki/Latvian_language>`__
mg  `Malagasy <https://en.wikipedia.org/wiki/Malagasy_language>`__
mk  `Macedonian <https://en.wikipedia.org/wiki/Macedonian_language>`__
ml  `Malayalam <https://en.wikipedia.org/wiki/Malayalam>`__
mn  `Mongolian <https://en.wikipedia.org/wiki/Mongolian_language>`__ (Cyrillic)
mr  `Marathi <https://en.wikipedia.org/wiki/Marathi_language>`__
ms  `Malay <https://en.wikipedia.org/wiki/Malay_language>`__
mt  `Maltese <https://en.wikipedia.org/wiki/Maltese_language>`__
nb  `Norwegian Bokmål <https://en.wikipedia.org/wiki/Bokm%C3%A5l>`__
ne  `Nepali <https://en.wikipedia.org/wiki/Nepali_language>`__
nl  `Dutch <https://en.wikipedia.org/wiki/Dutch_language>`__
nn  `Norwegian Nynorsk <https://en.wikipedia.org/wiki/Nynorsk>`__
no  Norwegian (generic)
oc  `Occitan <https://en.wikipedia.org/wiki/Occitan_language>`__
or  `Oriya <https://en.wikipedia.org/wiki/Oriya_language>`__
pa  `Punjabi <https://en.wikipedia.org/wiki/Punjabi_language>`__
pl  `Polish <https://en.wikipedia.org/wiki/Polish_language>`__
ps  `Pashto <https://en.wikipedia.org/wiki/Pashto_language>`__
pt  `Portuguese <https://en.wikipedia.org/wiki/Portuguese_language>`__
ro  `Romanian <https://en.wikipedia.org/wiki/Romanian_language>`__
ru  `Russian <https://en.wikipedia.org/wiki/Russian_language>`__
rw  `Kinyarwanda <https://en.wikipedia.org/wiki/Kinyarwanda>`__
se  `Northern Sami <https://en.wikipedia.org/wiki/Sami_languages>`__
si  `Sinhala <https://en.wikipedia.org/wiki/Sinhala_language>`__
sk  `Slovak <https://en.wikipedia.org/wiki/Slovak_language>`__
sl  `Slovenian <https://en.wikipedia.org/wiki/Slovenian_language>`__
sq  `Albanian <https://en.wikipedia.org/wiki/Albanian_language>`__
sr  `Serbian <https://en.wikipedia.org/wiki/Serbian_language>`__
sv  `Swedish <https://en.wikipedia.org/wiki/Swedish_language>`__
sw  `Swahili <https://en.wikipedia.org/wiki/Swahili_language>`__
ta  `Tamil <https://en.wikipedia.org/wiki/Tamil_language>`__
te  `Telugu <https://en.wikipedia.org/wiki/Telugu_language>`__
th  `Thai <https://en.wikipedia.org/wiki/Thai_language>`__
tl  `Tagalog <https://en.wikipedia.org/wiki/Tagalog_language>`__
tr  `Turkish <https://en.wikipedia.org/wiki/Turkish_language>`__
ug  `Uyghur <https://en.wikipedia.org/wiki/Uyghur_language>`__
uk  `Ukrainian <https://en.wikipedia.org/wiki/Ukrainian_language>`__
ur  `Urdu <https://en.wikipedia.org/wiki/Urdu>`__
vi  `Vietnamese <https://en.wikipedia.org/wiki/Vietnamese_language>`__
vo  `Volapük <https://en.wikipedia.org/wiki/Volap%C3%BCk>`__
wa  `Walloon <https://en.wikipedia.org/wiki/Walloon_language>`__
zh  `Chinese <https://en.wikipedia.org/wiki/Chinese_language>`__
==  ===========================

Languages covered by the default model, but not yet the test suite
------------------------------------------------------------------

==  =======
qu  `Quechua <https://en.wikipedia.org/wiki/Quechuan_languages>`__
xh  `Xhosa <https://en.wikipedia.org/wiki/Xhosa_language>`__
zu  `Zulu <https://en.wikipedia.org/wiki/Zulu_language>`__
==  =======

Languages in the test suite but not recognized by the default model
-------------------------------------------------------------------

===  =================
ada  `Adangme <https://en.wikipedia.org/wiki/Dangme_language>`__
arn  `Mapudungun <https://en.wikipedia.org/wiki/Mapuche_language>`__
arp  `Arapaho <https://en.wikipedia.org/wiki/Arapaho_language>`__
ast  `Asturian <https://en.wikipedia.org/wiki/Asturian_language>`__
ceb  `Cebuano <https://en.wikipedia.org/wiki/Visayan_languages>`__
csb  `Kashubian <https://en.wikipedia.org/wiki/Kashubian_language>`__
fur  `Friulian <https://en.wikipedia.org/wiki/Friulian_language>`__
fy   `West? Frisian <https://en.wikipedia.org/wiki/Frisian_languages>`__
gd   `Scottish Gaelic <https://en.wikipedia.org/wiki/Scottish_Gaelic>`__
ia   `Interlingua <https://en.wikipedia.org/wiki/Interlingua>`__
ilo  `Ilokano <https://en.wikipedia.org/wiki/Ilokano_language>`__
iu   `Inuktitut <https://en.wikipedia.org/wiki/Inuktitut>`__
kha  `Khasi <https://en.wikipedia.org/wiki/Khasi_language>`__
kld  `Gamilaraay <https://en.wikipedia.org/wiki/Gamilaraay_language>`__
lad  `Ladino <https://en.wikipedia.org/wiki/Judaeo-Spanish>`__
mi   `Māori <https://en.wikipedia.org/wiki/M%C4%81ori_language>`__
myn  `Mayan <https://en.wikipedia.org/wiki/Mayan_languages>`__
nah  `Nahuatl <https://en.wikipedia.org/wiki/Nahuatl>`__
nap  `Neapolitan <https://en.wikipedia.org/wiki/Neapolitan_language>`__
oj   `Ojibwe <https://en.wikipedia.org/wiki/Ojibwe_language>`__
rmq  `Caló <https://en.wikipedia.org/wiki/Cal%C3%B3_language>`__
xmm  `Manado Malay <https://en.wikipedia.org/wiki/Manado_Malay>`__
===  =================

Other languages with more than 7.4 million native speakers
----------------------------------------------------------

according to `Wikipedia's list
<https://en.wikipedia.org/wiki/List_of_languages_by_number_of_native_speakers>`__,
and treating all varieties of Chinese as one language.

===  ===========================
ak   `Akan <https://en.wikipedia.org/wiki/Akan_language>`__
awa  `Awadhi <https://en.wikipedia.org/wiki/Awadhi_language>`__
bal  `Balochi <https://en.wikipedia.org/wiki/Balochi_language>`__
bgc  `Haryanvi <https://en.wikipedia.org/wiki/Haryanvi_language>`__
bho  `Bhojpuri <https://en.wikipedia.org/wiki/Bhojpuri_language>`__
ctg  `Chittagonian <https://en.wikipedia.org/wiki/Chittagonian_language>`__
dcc  `Dakhini <https://en.wikipedia.org/wiki/Dakhini>`__
dhd  `Dhundari <https://en.wikipedia.org/wiki/Dhundari_language>`__
ff   `Fula <https://en.wikipedia.org/wiki/Fula_language>`__
ha   `Hausa <https://en.wikipedia.org/wiki/Hausa_language>`__
hil  `Hiligaynon <https://en.wikipedia.org/wiki/Hiligaynon_language>`__
hmv  `Hmong <https://en.wikipedia.org/wiki/Hmong_language>`__
hne  `Chhattisgarhi <https://en.wikipedia.org/wiki/Chhattisgarhi_language>`__
ig   `Igbo <https://en.wikipedia.org/wiki/Igbo_language>`__
kok  `Konkani <https://en.wikipedia.org/wiki/Konkani_language>`__
mad  `Madurese <https://en.wikipedia.org/wiki/Madurese_language>`__
mag  `Magahi <https://en.wikipedia.org/wiki/Magahi_language>`__
mai  `Maithili <https://en.wikipedia.org/wiki/Maithili_language>`__
mos  `Mossi <https://en.wikipedia.org/wiki/Mossi_language>`__
mwr  `Marwari <https://en.wikipedia.org/wiki/Marwari_language>`__
my   `Burmese <https://en.wikipedia.org/wiki/Burmese_language>`__
ny   `Chewa <https://en.wikipedia.org/wiki/Chewa_language>`__
om   `Oromo <https://en.wikipedia.org/wiki/Oromo_language>`__
rn   `Kirundi <https://en.wikipedia.org/wiki/Kirundi>`__
sd   `Sindhi <https://en.wikipedia.org/wiki/Sindhi_language>`__
skr  `Saraiki <https://en.wikipedia.org/wiki/Saraiki_language>`__
sn   `Shona <https://en.wikipedia.org/wiki/Shona_language>`__
so   `Somali <https://en.wikipedia.org/wiki/Somali_language>`__
su   `Sundanese <https://en.wikipedia.org/wiki/Sundanese_language>`__
syl  `Sylheti <https://en.wikipedia.org/wiki/Sylheti_language>`__
uz   `Uzbek <https://en.wikipedia.org/wiki/Uzbek_language>`__
yo   `Yoruba <https://en.wikipedia.org/wiki/Yoruba_language>`__
za   `Zhuang <https://en.wikipedia.org/wiki/Zhuang_languages>`__
===  ===========================
