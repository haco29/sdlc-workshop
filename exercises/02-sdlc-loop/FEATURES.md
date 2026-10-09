# Feature menu

Pick **one** feature and take it through the whole loop. Each one is small on purpose and
**deliberately vague**, so `/spec` has real questions to ask you and `/plan` has real
decisions to make. Aim for one or two files of change.

> Everyone building the same thing? Pick **#1**.

---

### 1. ⭐ Percentages and a winner (recommended)

Show each option's share of the vote, like `42%`, and mark the leader with 🏆.

- **Questions to settle in `/spec`:** How do you round, and must the shares add up to 100%?
  What does a poll with **zero votes** show? What if two options **tie** for the lead? In
  what order are the results listed?
- **Tests worth writing first:** zero votes, an exact tie, rounding that doesn't add up.

### 2. Close and reopen a poll

A **Close poll** button stops voting and shows the final result. **Reopen** allows voting
again.

- **Questions:** What happens to a vote cast after closing? Who's allowed to close? Does the
  closed state survive a page refresh?
- **Tests worth writing first:** the open → closed → open transitions, and that a closed
  poll rejects votes.

### 3. Pick more than one option

Let a voter choose several options in one vote.

- **Questions:** Is there a maximum, or a minimum? Is choosing nothing a valid vote? How
  does the total count: voters, or choices?
- **Tests worth writing first:** counting a multi-choice vote, and the limits.

### 4. Edit the options after creating the poll

Let the creator add, rename or remove options.

- **Questions:** What happens to votes on an option you remove, or rename? Can a rename
  create a duplicate? Can the poll drop below two options?
- **Tests worth writing first:** each edit operation, and that the totals stay consistent.

### 5. One vote per person

Ask voters for a name, and allow one vote each.

- **Questions:** Is the name case-sensitive? Can someone change their vote? What does a
  person who has already voted see?
- **Tests worth writing first:** a second vote under the same name, and changing a vote if
  that's allowed.

---

### Stretch goals, if you finish early

- Refresh the results automatically, so a room watching sees votes arrive.
- Export the results to CSV.
