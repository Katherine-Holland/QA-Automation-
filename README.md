# 🐺 Smart QA Helper

A lightweight web analysis tool to help **QA Engineers** and **testers** quickly generate Playwright test suggestions from any website.

---

## ✨ What It Does

- Scrapes a provided URL using BeautifulSoup.
- Detects common web elements:
  - Forms
  - Input fields
  - Buttons
  - Navigation links
- Suggests categorised Playwright tests with:
  - Clean, reusable code snippets
  - Smart selector strategies (`data-testid` > `id` > visible text fallback)
  - Visual badges showing the selector reliability
- Helps build **stable, production-quality tests faster** — especially useful when DevTools/Inspect isn't easily available.

---

## 🧪 Example Use Case

- Enter a website URL.
- Instantly receive:
  - Categorised test suggestions.
  - Example Playwright snippets.
  - Recommended selectors based on best practices.

Example output:
```python
# Example: Click button 'Submit'
page.click('[data-testid="submit-button"]')
```
> 🏷️ Selector Strategy: data-testid ✅

---

## 🚀 Live Demo

Try it here:  
👉 [https://automated-debug.onrender.com/](https://automated-debug.onrender.com/)

---

## ⚡ Technical Details

- **Frontend:** Streamlit (Python)
- **Backend:** BeautifulSoup (HTML parsing)
- **Playwright Language:** Python
- **Deployment:** Render (Docker-free)

---

## 🎯 Future Improvements (Optional)

- Skip or flag non-unique or unstable selectors.
- Allow custom selector strategy preferences (e.g., always prefer `id`).
- Export all suggested tests into a `.spec.ts` or `.spec.py` starter file.
