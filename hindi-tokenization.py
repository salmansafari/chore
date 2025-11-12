from indicnlp.tokenize import indic_tokenize
text = "मैं एमसीसी का छात्र हूँ."

#word tokenization
tokens = list(indic_tokenize.trivial_tokenize(text))
print("word tokens: ",tokens)

# or

!pip install torch==1.3.1+cpu -f https://download.pytorch.org/whl/torch_stable.html
!pip install inltk
!pip install tornado==4.5.3
from inltk.inltk import setup
setup('hi')
from inltk.inltk import tokenize
hindi_text = """प्राकृ तिक भाषा सीखना बहुि तिलचस्प है।"""
# tokenize(input text, language code)
tokenize(hindi_text, "hi")