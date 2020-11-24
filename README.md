# toggl-history

**Warning** toggl-history is a work in progress and currently not functional

toggl-history is a tool for keeping tabs on closed Toggl months and any changes made to them afterwards

## The problem

It's early November, everyone has dutifully updated their Toggl entries for October. _Meowth_ closes the month and sends invoices to our clients.

_Smeargle_ realizes they forgot to log the meeting they held at a customer. They go back to October and update their entries. They'll inform _Meowth_ the next day.

Of course, having a track record of forgetfulness, _Smeargle_ forgets to inform _Meowth_, who has no way of knowing the closed month was changed. The meeting time will never be billed.

## The proposed solution

### Finding changes to closed months

When closing a month, we query Toggl time entries for previous months in the current fiscal year.
Each month's result gets committed to a separate branch of a dedicated git repository:

```bash
$ git log --oneline january february

*    bb222 - "Entries for January on 01-05-2020" (january)
|  * 33ccc - "Entries for February on 01-05-2020" (february)
*  | bb222 - "Entries for January on 01-04-2020"
|  * 22bbb - "Entries for February on 01-04-2020"
*  | bb222 - "Entries for January on 01-03-2020"
|  * 11aaa - "Entries for February on 01-03-2020"
* /  aa111 - "Entries for January on 01-02-2020"
* fffff - "Fiscal year root commit"
```

This'll allow us to run diffs between the state of those months to see if they've changed.
If there are changes, we can visualise them and show them to _Meowth_.

### Visualising changes

Visualising the changes will be a bit more intense, but manageable.

Given a month (M) and two points in time (S, E):

- Parse the committed time entries for M(S) and M(E)
- For each entry in M(S):
  - Find a matching entry in M(E) using the entry ID
  - Found:
    - Output any differences in project, task or time
  - Not found:
    - Output as missing
  - Remove the matching entry from M(E)
- For each remaining entry in M(E):
  - Output as new
- Summarize the results
- Ship them off to _Meowth_
