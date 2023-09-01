import asyncio
import websockets

async def server(websocket, path):
    try:
        async for message in websocket:
            print(f"Received from client: {message}")
            await websocket.send(f"Server received: {message}")
    except websockets.ConnectionClosed:
        print("Client disconnected")

start_server = websockets.serve(server, "localhost", 3000)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
