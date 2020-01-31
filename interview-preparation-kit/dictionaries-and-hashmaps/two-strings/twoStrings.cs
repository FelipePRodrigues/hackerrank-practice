static string twoStrings(string s1, string s2) {
    List<char> characters = new List<char>();

        string menor, maior;

        if (s1.Length > s2.Length)
        {
            menor = s2;
            maior = s1;
        }
        else
        {
            menor = s1;
            maior = s2;
        }

        for (int i = 0; i < maior.Length; i++)
        {
            if (!characters.Contains(maior[i]))
            {
                characters.Add(maior[i]);
            }
        }

        for (int j = 0; j < menor.Length; j++)
        {
            if(characters.Contains(menor[j]))
                return "YES";
        }

        return "NO";
}