#hazm  0.7.0
#nltk 3.3

from Persian_Normalization import Persian_Normalizer
from Toeknization import Tokenization
from Jacard import JacardSimilarity
from Cosine import CosineSimilarity
from Lemmization import Lemmiz

persian_norm=Persian_Normalizer()
persian_norm.persian_normalizer('«برداشت کارشناسی»، «جو روانی» و «بازارهای رقیب» قابل محاسبه و تحٶلیل است که')
persian_token=Tokenization()
persian_token.token(persian_norm.result)

persian_norm1=Persian_Normalizer()
persian_norm1.persian_normalizer(' فوتبالی اش اشنایی دارند. او در سال ۱۳۹۳ از دنیای فوتبال خداحافظی کرد. شب گذشته مجی')

persian_token1=Tokenization()
persian_token1.token(persian_norm1.result)
#print(persian_token.token_query)
persian_lemm=Lemmiz()
persian_lemm.lemmiz(persian_token.token_query,persian_token1.token_query)

persian_jaccard=JacardSimilarity()
persian_jaccard.jacardsimilarity(persian_lemm.lem_string_1,persian_lemm.lem_string_2)

persian_cosine=CosineSimilarity()
persian_cosine.cosinesimilarity(persian_lemm.lem_string_1,persian_lemm.lem_string_2)





