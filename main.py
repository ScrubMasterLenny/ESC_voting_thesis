from data_extraction import *
from contest import *

rule_1975_2015 = Rule([12,10,8,7,6,5,4,3,2,1], 10)
ESC_classified = dict_to_classes(import_scores(), rule_1975_2015)

for ESC in ESC_classified:
    print("### ESC " + ESC + " ###")
    ESC_classified[ESC].print_result()
