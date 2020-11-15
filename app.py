import json

import jinja2
from jinja2 import Template
import requests as r
import pdfkit

dialog = [
 ]

word_count = 0
gripsum_uri = "http://127.0.0.1:8081/getIpsumSentence"
chatbot_uri = "http://127.0.0.1:5000/get"
while word_count < 50000:
    grindr_req = r.get(gripsum_uri)
    sentence = grindr_req.text
    dialog.append({"speaker": "BOTTOM", "words": sentence})
    word_count = word_count + len(sentence.split())

    # json_request = json.dumps()
    bot_req = r.get(chatbot_uri, params= {"msg": sentence} )
    bot_sentence = bot_req.text
    dialog.append({"speaker": "MARXBOT", "words": bot_sentence})
    word_count = word_count + len(bot_sentence.split())

    print(word_count)




templateLoader = jinja2.FileSystemLoader(searchpath="./")
templateEnv = jinja2.Environment(loader=templateLoader)
TEMPLATE_FILE = "screenplay.html"
template = templateEnv.get_template(TEMPLATE_FILE)
outputText = template.render(dialog=dialog)  # this is where to put args to the template renderer

print(outputText)

Html_file= open("screenplay1.html","w")
Html_file.write(outputText)
Html_file.close()

pdfkit.from_file('screenplay1.html', 'BottomVsBot.pdf')

# template = Template()
# msg = template.render('screenplay.html',)
# print(msg)

"""
<code>
<ul class="screenbox">
<li class="sceneheader">EXT. FOREST / ELSEWHERE – DAY</li>
<li class="action">Susan is on a cell-phone call. She smiles at Melissa, who walks by with two cups of coffee.</li>
<li class="character">SUSAN (V.O.)</li>
<li class="dialogue">Right now, this is probably our top pilot. But things change.</li>
</ul>

.screenbox {
    list-style: none;
    width: 420px;
    background: #eee;
    border: 1px solid #333;
    padding: 5px 14px;
}

.screenbox li { font: 12px/14px Courier, fixed; }

.sceneheader, .action, .character { padding-top: 1.5ex; }

.action { padding-right: 5%; }

.character { margin-left: 40%; }

.dialogue { margin-left: 25%; padding-right: 25%; }

.parenthetical { margin-left: 32%; padding-right: 30%; }

/* special case: dialogue followed by a parenthetical; the extra line needs to be suppressed */

.dialogue + .parenthetical { padding-bottom: 0; }

.transition { padding-top: 3ex; margin-left: 65%; padding-bottom: 1.5ex; }
"""