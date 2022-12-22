--- Text processing utilities.
--
-- This provides a Template class (modeled after the same from the Python
-- libraries, see string.Template). It also provides similar functions to those
-- found in the textwrap module.
--
-- IMPORTANT: this module has been deprecated and will be removed in a future
-- version (2.0). The contents of this module have moved to the `lib.stringx`
-- module.
--
-- See  @{03-strings.md.String_Templates|the Guide}.
--
-- Dependencies: `lib.stringx`, `lib.utils`
-- @module lib.text

local utils = require("lib.utils")

utils.raise_deprecation {
  source = "Penlight " .. utils._VERSION,
  message = "the contents of module 'lib.text' has moved into 'lib.stringx'",
  version_removed = "2.0.0",
  deprecated_after = "1.11.0",
  no_trace = true,
}

return require "lib.stringx"
