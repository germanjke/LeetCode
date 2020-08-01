class Solution {
    public String reverseWords(String s) {
        String[] words = s.trim().split(" +"); // " +" means multi spaces
        Collections.reverse(Arrays.asList(words));
        return String.join(" ",words);
    }
}
