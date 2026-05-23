from http.server import BaseHTTPRequestHandler
import json,os,asyncio,sys
sys.path.insert(0,os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from botlogic import setup_app
from telegram import Update
BOT_TOKEN=os.getenv("BOT_TOKEN","8916888298:AAEIuLU0f4n_DuVXNhKj5bs22D5LtS0eWHA")
class handler(BaseHTTPRequestHandler):
 def do_POST(self):
  length=int(self.headers['Content-Length'])
  body=self.rfile.read(length)
  async def process():
   app=setup_app(BOT_TOKEN)
   await app.initialize()
   update=Update.de_json(json.loads(body),app.bot)
   await app.process_update(update)
   await app.shutdown()
  asyncio.run(process())
  self.send_response(200)
  self.end_headers()
  self.wfile.write(b'OK')
 def do_GET(self):
  self.send_response(200)
  self.end_headers()
  self.wfile.write(b'EmonEarningBot is running!')
