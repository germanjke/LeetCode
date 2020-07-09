class Solution:
    def arrangeWords(self, text: str) -> str:
        words = text.split(" ") #split string
        list_of_lenghts = [] #create list with lenghts of words
        list_of_names = [] #create list with names of words 
        for i in words:
            list_of_names.append(i.lower())  #dont forget to make all to lower case
            list_of_lenghts.append(len(i)) 
        dict_with_lens = {} #new dict with format {len:name}
        for k,v in zip(list_of_lenghts, list_of_names):
            dict_with_lens.setdefault(k, []).append(v)
        dict_with_lens_new = dict(sorted(dict_with_lens.items())) #sort dict by keys (lens)
        final_names = [] #final list with names
        for i in dict_with_lens_new.values():
            final_names.extend(i) #add all names sorted by keys
        final_names[0] = final_names[0].title() #change first name to title
        return ' '.join(final_names) #join
