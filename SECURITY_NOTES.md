# Security baseline
2026-10-28

- Anonymous GET /recipes → 200 OK, returns all recipes including is_public: false
- Anonymous PATCH /recipes/2 → 200 OK, updates title to "Hacked overnight oats"
- Anonymous DELETE /recipes/2 → 204 No Content (or 200), recipe 2 no longer appears in GET /recipes