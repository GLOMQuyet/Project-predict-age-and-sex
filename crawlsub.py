with open('Deep Learning 19_ (1) Variational AutoEncoder _ Introduction and Probability Refresher.srt','r') as f:
    x = f.read()
    x = x.replace('ï»¿','')
import re
TAG_RE = re.compile(r'<[^>]+>')
def remove_tags(x):
    return TAG_RE.sub('', x)

with open('VAE.srt','w') as f:
    y = f.write(remove_tags(x))
    print(y)