class Solution:

    #Function to perform choose and swap operation.
    def chooseandswap(self, str):
        #converting the string into a set to remove duplicate characters.
        ss = set(list(str))

        #iterating over the string
        for i in range(len(str)):

            #if the current character is present in the set,
            #we remove it from the set.
            if str[i] in ss:
                ss.remove(str[i])

            #if the set is empty, which means we have removed
            #all the characters, we break the loop.
            if len(ss) == 0:
                break

            #if the minimum character in the set is less than the
            #current character, we perform choose and swap operation.
            if min(ss) < str[i]:
                temp = str[i]
                #replacing the current character with '$' for temporary storage.
                str = str.replace(str[i], "$")
                #replacing the minimum character with the current character.
                str = str.replace(min(ss), temp)
                #replacing '$' with the minimum character.
                str = str.replace("$", min(ss))
                break

        #returning the modified string after choose and swap operation.
        return str