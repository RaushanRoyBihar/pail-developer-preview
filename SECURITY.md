# Security

Do not report private datasets, credentials, or customer evidence in public
issues. For a suspected exposure, contact the repository owner privately through
the GitHub profile.

The public repository contains no PAIL engine. A deployed gateway must enforce
authentication, tenant isolation, request limits, secure key management,
logging, and upstream timeouts. Browser code must never receive private API
tokens or runtime addresses.

Supported public surfaces are listed in `public-manifest.json`. Anything else
should be treated as private until explicitly reviewed.
