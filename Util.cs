using System;

namespace Core {
    static class Util {
        public static void PrintStartup(DateTime now, CompressSettings settings) {
            Console.ForegroundColor = ConsoleColor.Green;
            Console.WriteLine($"Started:    {now}");

            string threads = (settings.ThreadCount > 1) 
                ? "[MULTI-THREADING]" : "[SINGLE-THREADING]";

            Console.WriteLine($"Threads:    {settings.ThreadCount} {threads}");
            Console.WriteLine($"Chunk size: {settings.SearchSize} Chars");
            Console.WriteLine($"Block size: {settings.BlockBytes} Bytes");
            Console.WriteLine();
            Console.ForegroundColor = ConsoleColor.White;
        }


        public static int NextPow2(int n) {
            return (int)Math.Ceiling(Math.Log10(n) / Math.Log10(2));
        }
    }
}