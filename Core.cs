using System;
using System.Collections.Generic;

namespace Core {
    class PiFSEngine {

        public CompressSettings Settings {get; private set;}

        // Constructors -------------------------------------------------------
        public PiFSEngine(CompressSettings settings) {
            Settings = settings;
        }
        public PiFSEngine() {
            // Use default settings -------------------------------------------
            CompressSettings defaultSettings = new CompressSettings(
                "abcdefghijklmnopqrstuvwxyzåäö .,!?",
                50000000,
                8
            );

            Settings = defaultSettings;
        }

        // Compression Algorithm ----------------------------------------------
        public string Compress(string data) {return "";}
        public List<int> CompressToList(string data) {


            DateTime start = DateTime.Now;
            Util.PrintStartup(start, Settings);

            // oki rip

            int alphaCount = Settings.Alphanumerics.Length;
            int bytesNeeded = Util.NextPow2(alphaCount);

            // sämst kod sopa
            string dec = "";
            foreach(char character in data) {
                dec += (string)Settings.Alphanumerics.IndexOf(character) + ";";
            }

            int binary = string.;

            return new List<int>();
        }
        public string Decompress(string code) {
            return "";
        }
    }

    struct CompressSettings {
        // Constants ----------------------------------------------------------
        // Allowed characters in file
        public string Alphanumerics {get; set;}
        public int ThreadCount {get; set;}
        public int SearchSize {get; set;}
        public int BlockBytes {get; set;}

        public CompressSettings(string abc, int searchSize, int blockBytes) {
            Alphanumerics = abc;
            ThreadCount = 1;
            SearchSize = searchSize;
            BlockBytes = blockBytes;
        }
    }
}