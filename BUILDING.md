# Building

## Build

```console
uv build
```

## Publish

_Get token from https://pypi.org/manage/account/token/ _

```console
uv build
UV_PUBLISH_TOKEN="your pypi token" uv publish
```

## Test

```console
uv run pytest -s .
```

## Debugging

Use [delta](https://github.com/dandavison/delta)

```console
delta input.txt output.txt
```
