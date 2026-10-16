# Operationalization Guide

## Tableau MCP
Official server: https://github.com/tableau/tableau-mcp

### Hosted (Tableau Cloud)
Point MCP clients at `https://mcp.tableau.com` and complete OAuth.

### Self-hosted (npx)
```json
{
  "mcpServers": {
    "tableau": {
      "command": "npx",
      "args": ["-y", "@tableau/mcp-server@latest"],
      "env": {
        "SERVER": "https://your-pod.online.tableau.com",
        "SITE_NAME": "your-site",
        "PAT_NAME": "your-pat-name",
        "PAT_VALUE": "your-pat-secret"
      }
    }
  }
}
```

## Synthetic Data MCP
AWS Labs: `awslabs.syntheticdata-mcp-server` (uvx installable) for business-description driven generation and validation.

## Hyper + Publishing Path
1. Run `python generate_reentry_data.py` to produce CSV.
2. Convert to `.hyper` with Tableau Hyper API (`tableauhyperapi`).
3. Publish via Tableau Server Client (`tableauserverclient`) using PAT.

See `.github/workflows/generate-and-publish.yml` for a skeleton.

## Required Secrets (GitHub)
- `TABLEAU_SERVER_URL`
- `TABLEAU_SITE_ID`
- `TABLEAU_PAT_NAME`
- `TABLEAU_PAT_SECRET`
- `TABLEAU_PROJECT_NAME`

## Next Steps
- Add PAT secrets in repo Settings → Secrets.
- Uncomment and complete the workflow.
- Generate CSV locally or in CI, convert to Hyper, publish.
