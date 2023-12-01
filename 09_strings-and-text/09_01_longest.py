# Which of the following strings is the longest?
# Use the len() function to find out.

longest_german_word = "Donaudampfschifffahrtsgesellschaftskapitänskajütentürschnalle"
longest_hungarian_word = "Megszentségteleníthetetlenségeskedéseitekért"
longest_finnish_word = "Lentokonesuihkuturbiinimoottoriapumekaanikkoaliupseerioppilas"
strong_password = "%8Ddb^ca<*'{9pur/Y(8n}^QPm3G?JJY}\(<bCGHv^FfM}.;)khpkSYTfMA@>N"

longest_str = None
len_longest = 0
for s in [longest_german_word, longest_hungarian_word, longest_finnish_word, strong_password]:
    if len(s) > len_longest:
        longest_str = s
        len_longest = len(s)

print("The longest string is\n" + longest_str + "\n" + "at " + str(len_longest) + " characters.")