using System;

namespace Aoc2019CS
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Advent of code!");

            Day01 a = new Day01();

            int task1 = a.task1();
            Console.WriteLine("day 01 task 1: " + task1);
            
        }
    }
}
