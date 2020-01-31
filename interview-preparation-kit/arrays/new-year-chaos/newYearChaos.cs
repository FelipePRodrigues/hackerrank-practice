static void minimumBribes(int[] q)
        {
            int bribesCount = 0;

            if (isTooChaotic(q))
            {
                Console.WriteLine("Too chaotic");
                return;
            }
            else
            {
                while (findIndexToBribe(q) != -1)
                {
                    q = bribeElements(q, findIndexToBribe(q));
                    bribesCount++;
                }
            }

            Console.WriteLine(bribesCount.ToString());
        }

        static bool isTooChaotic(int[] line)
        {

            for (int i = 0; i < line.Length; i++)
            {

                int indexInLine = Array.IndexOf(line, (i + 1));

                if (isTooFarToReturn(indexInLine, i))
                {
                    return true;
                }
            }

            return false;
        }

        static bool isTooFarToReturn(int indexInLine, int targetIndex)
        {
            if ((targetIndex > indexInLine) && (targetIndex - indexInLine > 2))
            {
                return true;
            }
            else
            {
                return false;
            }
        }

        static int[] bribeElements(int[] line, int index)
        {

            int indexElement = line[index];

            line[index] = line[index + 1];
            line[index + 1] = indexElement;

            return line;
        }

        static int findIndexToBribe(int[] line)
        {
            for (int i = (line.Length - 1); i >= 0; i--)
            {
                if (line[i] != (i + 1))
                {
                    int indexToBribe = Array.IndexOf(line, (i + 1));
                    return indexToBribe;
                }
            }

            return -1;
        }