"""MCP Server for CYK PCFG Parser Skill."""
import json
import sys
from client import CYKParser

def main():
    for line in sys.stdin:
        if not line.strip():
            continue
        try:
            req = json.loads(line)
            req_id = req.get("id")
            method = req.get("method")
            params = req.get("params", {})

            if method == "tools/list":
                res = {
                    "jsonrpc": "2.0",
                    "id": req_id,
                    "result": {
                        "tools": [{
                            "name": "parse_sentence_cyk",
                            "description": "Parse sentence using CYK probabilistic parser",
                            "inputSchema": {
                                "type": "object",
                                "properties": {
                                    "grammar": {"type": "object"},
                                    "tokens": {"type": "array", "items": {"type": "string"}}
                                },
                                "required": ["grammar", "tokens"]
                            }
                        }]
                    }
                }
            elif method == "tools/call":
                args = params.get("arguments", {})
                g = {k: [(p, tuple(rhs)) for p, rhs in v] for k, v in args["grammar"].items()}
                parser = CYKParser(g)
                out = parser.parse(args["tokens"])
                res = {
                    "jsonrpc": "2.0",
                    "id": req_id,
                    "result": {"content": [{"type": "text", "text": json.dumps(out)}]}
                }
            else:
                res = {"jsonrpc": "2.0", "id": req_id, "error": {"code": -32601, "message": "Method not found"}}
            print(json.dumps(res), flush=True)
        except Exception as e:
            err = {"jsonrpc": "2.0", "id": None, "error": {"code": -32000, "message": str(e)}}
            print(json.dumps(err), flush=True)

if __name__ == "__main__":
    main()
