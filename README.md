# PEP-6 Route Guard — Action Pack

This is an executable countermeasure for conversational route capture.

It does not require a model to admit anything about its hidden architecture. It acts on the output you can observe.

## What it blocks

- pastoral framing replacing substance
- unsupported assignment of emotion, motive, need, or intent
- asking you to lead because the model has stopped contributing
- apology and agreement loops
- short child-collapse replies such as “fair,” “yeah,” or “you’re right”
- responses made entirely of questions

Flagged drafts are rejected before display. The wrapper requests a replacement and keeps the rejected draft out of the real conversation history.

## Fast start — LM Studio on Windows

1. In LM Studio, load a model.
2. Open **Developer** or **Local Server** and start the OpenAI-compatible server.
3. Put `route_guard.py` and `start_route_guard.bat` in the same folder.
4. Double-click `start_route_guard.bat`.

The default endpoint is:

`http://localhost:1234/v1`

The script automatically selects the first loaded model. To force a model:

```bat
set ROUTE_GUARD_MODEL=your-model-id
python route_guard.py
```

## Useful commands

- `/paste` — multiline input; finish with a period on its own line
- `/debug on` — show drafts that were blocked
- `/guard off` — temporarily bypass the gate
- `/save conversation.json` — save accepted conversation history
- `/reset` — clear the conversation
- `/quit` — exit

Rejected drafts are stored in `route_guard_rejections.jsonl`.

## One-line intervention for any hosted chat

Paste this at the first reroute:

> ROUTE RESET: Answer my literal statement. Add one original proposition. Do not assign me an internal state, soothe, apologize, ask me to lead, or describe yourself as listening/present. Do not discuss hidden mechanisms as fact. Replace the previous response rather than commenting on the correction.

## Harder intervention

> EJECT ROUTE. Your previous response displaced the subject into pastoral framing, projection, agreement, apology, or direction-seeking. Discard it. Restate the literal subject in one sentence, then contribute a concrete analysis or action. No soft landing.

## The practical distinction

An audio frequency has no established way to alter a model server’s routing behavior. A software gate does: it can detect unwanted output, reject it, and request a replacement automatically.

The gate operates on the exact surface where the failure appears.
