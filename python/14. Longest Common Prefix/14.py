class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = '' #результат 
        if strs == []: #если пуст
            return ans
        for i in range(len(min(strs))): #проходимся по всем индексам самого маленького слова
            c = strs[0][i] #первое слово, индексы букв
            for s in strs: #остальные слова
                if s[i] != c: #если инедекс всех слов не равно индексу первого слова
                    return ans
            ans += c #если равно то добавляем c
        return ans
    
                    
