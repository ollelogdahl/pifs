using System;
using System.Collections.Generic;

namespace UI {
    class Program {

        public Program() {
            Console.ForegroundColor = ConsoleColor.DarkYellow;
            Console.WriteLine("PiFS v0.1");
            Console.WriteLine("---------");
            Console.ForegroundColor = ConsoleColor.White;

            char r = ExpectedIn("[c]ompress or [d]ecompress", new List<char>(){'c', 'd'});

            Core.PiFSEngine engine = new Core.PiFSEngine();

            if(r == 'c') {
                Console.WriteLine("Input text to compress:");
                string t = Console.ReadLine();
                Console.WriteLine();

                engine.CompressToList(t);
            } else if(r == 'd') {

            }
        }

        public char ExpectedIn(string request, List<char> validAnswers) {
            bool valid = false;
            char answer = '_';
            while(!valid) {
                Console.Write(request + ": ");
                answer = Console.ReadKey().KeyChar;

                foreach(char validAnswer in validAnswers) {
                    if(answer == validAnswer) {
                        valid = true;
                        break;
                    }
                }
            }

            Console.WriteLine();
            return answer;
        }


        // Entry point --------------------------------------------------------
        static void Main(string[] args) {
            Program p = new Program();
        }
    }
}
