Bankroll Manager

In this repository, I develop a program where you receive a suggestion of how much money to bet, based on your confidence level. The program calculates how much money is safe to bet, based on your bankroll.

What it does

You create a bankroll (a pot of money set aside for betting) and open bets connected to it. For each bet, the program asks how confident you are (as a percentage) and suggests how much of your current balance is reasonable to risk. Once you know the result, the bet updates your bankroll's balance automatically.

Design decisions
Bankroll and Bet are separate classes. A Bankroll only knows about money (its balance). A Bet knows about a single wager (odds, amount, result) and holds a reference to the Bankroll it belongs to.
A bet holds a reference to its bankroll, not a copy. This means a bet can read the bankroll's balance and update it directly through bank.saldo, instead of the bankroll having to track down each of its bets.
A bet's outcome starts as None (pending), not True/False, because a bet exists before its result is known. It only becomes True or False once resolver() is called.
The stake amount is calculated, not passed in. Instead of requiring a bet amount upfront, monto_a_Apostar() asks for a confidence percentage and calculates the amount from the bankroll's current balance — avoiding the circular problem of needing the answer before the question is asked.
Current status

This is an early-stage learning project. Right now it supports a single staking method (fixed percentage of the bankroll, chosen per bet). Planned next steps:

Support odds conversion between American and decimal formats
Add a betting history to Bankroll
Add a second staking method (Kelly Criterion)
Input validation for the initial bankroll amount
Why this project

Built to practice object-oriented Python — specifically how separate objects (a bankroll and its bets) reference and update each other — as part of my portfolio while learning to program.
