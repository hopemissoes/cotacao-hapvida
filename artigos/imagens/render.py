import asyncio, sys
from playwright.async_api import async_playwright
async def main(html, out, w=1200, h=630):
    async with async_playwright() as p:
        b = await p.chromium.launch(executable_path="/opt/pw-browsers/chromium-1194/chrome-linux/chrome",
                                    args=["--no-sandbox","--font-render-hinting=none"])
        pg = await b.new_page(viewport={"width":w,"height":h}, device_scale_factor=1)
        await pg.goto("file://"+html)
        await pg.wait_for_timeout(400)
        await pg.screenshot(path=out)
        await b.close()
asyncio.run(main(sys.argv[1], sys.argv[2]))
