# IPAEngine
International Phonetic Alphabet common word recognition engine

This project recognizes words of common origins in the same language or different languages. 
The recognition is based on International Phonetic Alphabet and the comparison is done on consonants only as consonants 
usually tend to bear meaning in words. The comparison results of ia given pair of words is persisted to sqlite.

The training data is generated containg 15000 pairs of compared words in the following languages: English, German, Russian, Hebrew, Mandarin, Persian. The training data is located in IPAEngine/ipa.sqlite, it can be downloaded and opened with sqlite.

This software is not in public domain, refer to Copyright file for copyright information. The results of the training data are available for public use by downloading ipa.sqlite file.

