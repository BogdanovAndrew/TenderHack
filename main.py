import validator
import standarter


req = "Мыло жыдкое 220 мл"

correct_req = standarter.stem_req(validator.correct_req(req))

print(correct_req)