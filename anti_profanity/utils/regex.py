import re

__all__ = ['RegexProc']

word_pattern = r'[А-яA-z0-9\-]+'


class RegexProc(object):
    PATTERN_RU = r'|'.join((
        r'(\b[сs]{1}[сsц]{0,1}[uуy](?:[ч4]{0,1}[иаakк][^ц])\w*\b)',
        r'(\b(?!пло|стра|[тл]и)(\w(?!(у|пло)))*[хx][уy](й|йа|[еeё]|и|я|ли|ю)(?!га)\w*\b)',
        r'(\b(п[oо]|[нз][аa])*[хx][eе][рp]\w*\b)',
        r'(\b[мm][уy][дd]([аa][кk]|[oо]|и)\w*\b)',
        r'(\b\w*д[рp](?:[oо][ч4]|[аa][ч4])(?!л)\w*\b)',
        r'(\b(?!(?:кило)?[тм]ет)(?!смо)[а-яa-z]*(?<!с)т[рp][аa][хx]\w*\b)',
        r'(\b[к|k][аaoо][з3z]+[eе]?ё?л\w*\b)',
        r'(\b(?!со)\w*п[еeё]р[нд](и|иc|ы|у|н|е|ы)\w*\b)',
        r'(\b\w*[бп][ссз]д\w+\b)',
        r'(\b([нnп][аa]?[оo]?[xх])\b)',
        r'(\b([аa]?[оo]?[нnпбз][аa]?[оo]?)?([cс][pр][аa][^зжбсвм])\w*\b)',
        r'(\b\w*([оo]т|вы|[рp]и|[оo]|и|[уy]){0,1}([пnрp][iиеeё]{0,1}[3zзсcs][дd])\w*\b)',
        r'(\b(вы)?у?[еeё]?би?ля[дт]?[юоo]?\w*\b)',
        r'(\b(?!вело|ски|эн)\w*[пpp][eеиi][дd][oaоаеeирp](?![цянгюсмйчв])[рp]?(?![лт])\w*\b)',
        r'(\b(?!в?[ст]{1,2}еб)(?:(?:в?[сcз3о][тяaа]?[ьъ]?|вы|п[рp][иоo]|[уy]|р[aа][з3z][ьъ]?|к[оo]н[оo])?[её]б[а-яa-z]*)|(?:[а-яa-z]*[^хлрдв][еeё]б)\b)',
        r'(\b[з3z][аaоo]л[уy]п[аaeеин]\w*\b)',
    ))

    regex = dict(
        ru=re.compile(PATTERN_RU, re.U | re.I),
        en=''
    )

    @staticmethod
    def detect(text, lang):
        if not text:
            return False
        regex = RegexProc.regex.get(lang)
        if regex:
            return bool(regex.findall(text))
        return False

    @staticmethod
    def replace(text, lang, repl='[censored]'):
        regex = RegexProc.regex.get(lang)
        if regex:
            return regex.sub(repl, text)
        return text

    @staticmethod
    def wrap(text, lang, wrap=('<span style="color:red;">', '</span>',)):
        words = {}
        regex = RegexProc.regex.get(lang)
        if regex:
            for word in re.findall(word_pattern, text):
                if len(word) < 3:
                    continue
                if regex.findall(word):
                    words[word] = f'{wrap[0]}{word}{wrap[1]}'
            for word, wrapped in words.items():
                text = text.replace(word, wrapped)
        return text
