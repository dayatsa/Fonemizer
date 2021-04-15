# Fonemizer Project
Fonemizer is use to convert Indonesian sentences into ARPABET

### Requirement
- arpabetandipaconvertor [Source Code](https://github.com/chdzq/ARPAbetAndIPAConvertor)

  `pip install -r requirements.txt`


### Example
- Initialization

  `from fonem import *`
  `converter = IndoARPA(separator=' ', res_ipa=True)`
- Convert Indo -> ARPABET

  `result = converter.indo2ARPA(<string>)`
