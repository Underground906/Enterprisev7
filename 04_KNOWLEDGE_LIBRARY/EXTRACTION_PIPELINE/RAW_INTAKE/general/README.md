# general/

Drop anything that doesn't fit the other categories here.

**What goes here:** Miscellaneous documents, notes, exports, anything you're not sure how to classify. The intake processor will attempt to route it.

**Format:** Any.

**What happens next:**
1. `intake_processor.py` scores against all 23 pillar keywords and routes accordingly
2. If it can't route confidently, it goes to `04_KNOWLEDGE_LIBRARY/ONGOING/UNROUTED/`
3. `v7_extract.py domains <file>` runs 27-domain classification

**Naming:** `YYYY-MM-DD_description.ext`
