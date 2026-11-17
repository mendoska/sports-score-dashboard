# Sports Score Dashboard

![tests](https://github.com/mendoska/sports-score-dashboard/actions/workflows/ci.yml/badge.svg)

A live scoreboard for NFL, NBA, and NHL games, pulling real-time data from ESPN's undocumented API. Games are sorted so live ones show first, then upcoming, then final.

**Live demo:** https://sports-scoring-app-ksa1.onrender.com/
(The free host sleeps after 15 minutes idle, so the first load can take 1-2 minutes.)

![](nfl-app.gif)

## Features
- Live scores for NFL, NBA, and NHL
- Games grouped by status: live, upcoming, final
- Dark mode toggle
- Responsive layout

## Tech stack
Flask (Python) · HTML/CSS/JavaScript · ESPN API · Render · pytest · GitHub Actions

## How it's tested
ESPN's responses change daily, so the tests never call ESPN. They use saved JSON responses (`tests/fixtures/`) and the `responses` library to stand in for the API, which keeps every run deterministic.

- Happy path: one game, all 8 output fields checked against known values
- No games on the scoreboard returns an empty list instead of crashing
- A `null` score from ESPN is handled
- Page-load checks for the routes
- GitHub Actions runs the suite on every push

```
pip install -r requirements.txt -r requirements-dev.txt
pytest
```

## A bug the tests caught
While writing the null-score test, I found that one `null` score from ESPN crashed the whole page with a `TypeError`. The code only used its default when the key was missing, not when it was present but empty. I filed it as Issue #3, fixed it, and the same test now guards against it coming back.

## Challenges
ESPN has no public documentation for this API, so I mapped the JSON structure by hand (events, then competitions, then competitors) and used AI to help break down the fields.

## Known limitations
- Timeouts and ESPN errors aren't handled yet. A failed request would break the page.
- Postponed and overtime games aren't tested yet
- The route tests only check that pages load, not that the data is correct

## Ideas for later
Player stats, odds, mobile UI improvements

*Built with AI assistance; design and test strategy are mine.*