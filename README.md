## genre-query-stats
Author: Joel Coddington-Lopez

---
This script calculates genre statistics for a given search term by utilizing the open-source [iTunes API](https://performance-partners.apple.com/search-api).

### Installation

Once you've cloned or downloaded this repo, make sure you have both Python & pip installed and run `pip install requests`.

To run the script, use `main.py` as the entrypoint.

```
> cd genre-query-stats
> python3 main.py
```

### Usage

When running this script, you will be prompted to enter a session name. This session name will be used to save query logs.

**Running a query:**

Entering a search term will query the iTunes API and return genre results. If no genre results are available, the script will notify you that 0 results were returned.
```
Enter a search term, or type `quit` to exit the program.
> the wizard of oz
> Loading... this may take a moment!
Out of 100 result(s) for the wizard of oz, 4 genre(s) were identified.
Here are the stats:
	- 95% - Soundtrack
	- 3% - Pop
	- 1% - Hip-Hop/Rap
	- 1% - Country
```

**Ending your session**

Quitting out of the program will automatically save session logs.

Note that existing log files with the same session name will be overwritten upon saving.

```
Enter a search term, or type `quit` to exit the program.
> quit
-----------------------------------
> Query engine has now shut down.
> Result logs are available in joel.txt
```