# Voice Agent

A real-time voice agent application built with LiveKit and various AI plugins.

> [!WARNING]
> **Python Version Requirement**
> This project requires **Python 3.10**. The currently tested version is **3.10.11**. 
> You can download it directly from here: [Python 3.10.11 (amd64)](https://www.python.org/ftp/python/3.10.11/python-3.10.11-amd64.exe)

## Environment Variables (.env)

Create a `.env` file in the root directory of the project with the following variables. Replace the values with your actual API keys and URLs:

```env
LIVEKIT_URL=your_livekit_url
LIVEKIT_API_KEY=your_livekit_api_key
LIVEKIT_API_SECRET=your_livekit_api_secret
ELEVEN_API_KEY=your_elevenlabs_api_key
LITELLM_API_KEY=your_litellm_api_key
DEEPGRAM_API_KEY=your_deepgram_api_key
```

## Dependencies (requirements.txt)

The project requires the following dependencies to be installed:

```text
python-dotenv==1.2.1
livekit-agents==1.5.7
livekit-plugins-deepgram==1.5.7
livekit-plugins-openai==1.5.7
livekit-plugins-elevenlabs==1.5.7
livekit-plugins-silero==1.5.7
```

*Note: You can install these via `pip install -r requirements.txt` if you create the file, or you can just run the `start.bat` script which handles the installation for you.*

## How to Run

To run the voice agent, ensure your `.env` file is set up correctly. Then, use one of the following methods:

**Option 1: Using the batch script (Windows)**
Simply execute the `start.bat` file. It will automatically install the required dependencies and launch the agent.
```cmd
start.bat
```

**Option 2: Running via Python**
If you have already installed the dependencies or are running it manually from a terminal, use the following command:
```cmd
python main.py dev
```

## Testing the Agent

Once the agent is running successfully in your terminal, you can interact with and test it by visiting the LiveKit Agents Playground:
[https://agents-playground.livekit.io/](https://agents-playground.livekit.io/)
