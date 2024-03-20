Issue: https://github.com/airtai/faststream/discussions/1320

1. Setup a jetstream named `product_feeds`
2. Setup consumer named `feeds_app`
3. Run docker-compose `docker-compose up -d`
4. Run the app `faststream run serve:app`
5. Push a message to the jetstream `nats pub product_feeds.feeds_update_requested ""`
6. Observe strange logs in console (unexpected calls to `feeds_update_requested`)

```log
Welcome to fish, the friendly interactive shell
Type help for instructions on how to use fish
[WARN] - (starship::config): Error in 'CmdDuration' at 'command_timeout': Unknown key

faststream-issue master 
.venv ❯ faststream run serve:app
2024-03-20 13:11:06,990 INFO     - FastStream app starting...
2024-03-20 13:11:06,998 INFO     - product_feeds | product_feeds.feeds_update_requested    |            - `UpdateFeeds` waiting for messages
2024-03-20 13:11:06,999 INFO     - product_feeds | product_feeds.one_feed_update_requested |            - `UpdateFeed` waiting for messages
2024-03-20 13:11:07,001 INFO     - FastStream app started successfully! To exit, press CTRL+C
2024-03-20 13:11:09,001 INFO     - product_feeds | product_feeds.feeds_update_requested    | 41b40328-5 - Received
2024-03-20 13:11:09,004 INFO     - product_feeds | product_feeds.feeds_update_requested    | 41b40328-5 - Updating feed; feed_id=1
2024-03-20 13:11:09,008 INFO     - product_feeds | product_feeds.feeds_update_requested    | 41b40328-5 - Processed
2024-03-20 13:11:11,005 INFO     - product_feeds | product_feeds.one_feed_update_requested | e80925b4-c - Received
2024-03-20 13:11:11,008 INFO     - product_feeds | product_feeds.one_feed_update_requested | e80925b4-c - Downloading feed; feed_id=1
2024-03-20 13:11:21,010 INFO     - product_feeds | product_feeds.one_feed_update_requested | e80925b4-c - Processing item; item_id=1 feed_id=1
2024-03-20 13:11:21,013 INFO     - product_feeds | product_feeds.one_feed_update_requested | e80925b4-c - Processing item; item_id=2 feed_id=1
2024-03-20 13:11:21,015 INFO     - product_feeds | product_feeds.one_feed_update_requested | e80925b4-c - Processing item; item_id=3 feed_id=1
2024-03-20 13:11:21,015 INFO     - product_feeds | product_feeds.feeds_update_requested    | 3e445659-e - Received
2024-03-20 13:11:21,016 INFO     - product_feeds | product_feeds.feeds_update_requested    | 7d3f95fb-7 - Received
2024-03-20 13:11:21,017 INFO     - product_feeds | product_feeds.one_feed_update_requested | e80925b4-c - Processing item; item_id=4 feed_id=1
2024-03-20 13:11:21,018 ERROR    - product_feeds | product_feeds.feeds_update_requested    | 3e445659-e - ValidationError: 1 validation error for update_feeds
msg
  Input should be a valid string [type=string_type, input_value={'item': {'id': 1, 'title...e': None}, 'feed_id': 1}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.6/v/string_type
Traceback (most recent call last):
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/handler.py", line 367, in consume
    raise e
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/handler.py", line 331, in consume
    result = await cast(
             ^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/utils.py", line 95, in set_message_wrapper
    return await func(message)
           ^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/nats/broker.py", line 244, in process_wrapper
    r = await func(message)
        ^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/core/asynchronous.py", line 406, in decode_wrapper
    return await func(msg)
           ^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/use.py", line 146, in injected_wrapper
    r = await real_model.asolve(
        ^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/core/model.py", line 519, in asolve
    final_args, final_kwargs, call = cast_gen.send(kwargs)
                                     ^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/core/model.py", line 274, in _solve
    casted_model = self.model(**solved_kw)
                   ^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/pydantic/main.py", line 171, in __init__
    self.__pydantic_validator__.validate_python(data, self_instance=self)
pydantic_core._pydantic_core.ValidationError: 1 validation error for update_feeds
msg
  Input should be a valid string [type=string_type, input_value={'item': {'id': 1, 'title...e': None}, 'feed_id': 1}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.6/v/string_type
2024-03-20 13:11:21,023 INFO     - product_feeds | product_feeds.feeds_update_requested    | 3e445659-e - Processed
2024-03-20 13:11:21,024 ERROR    - product_feeds | product_feeds.feeds_update_requested    | 7d3f95fb-7 - ValidationError: 1 validation error for update_feeds
msg
  Input should be a valid string [type=string_type, input_value={'item': {'id': 2, 'title...e': None}, 'feed_id': 1}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.6/v/string_type
Traceback (most recent call last):
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/handler.py", line 367, in consume
    raise e
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/handler.py", line 331, in consume
    result = await cast(
             ^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/utils.py", line 95, in set_message_wrapper
    return await func(message)
           ^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/nats/broker.py", line 244, in process_wrapper
    r = await func(message)
        ^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/core/asynchronous.py", line 406, in decode_wrapper
    return await func(msg)
           ^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/use.py", line 146, in injected_wrapper
    r = await real_model.asolve(
        ^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/core/model.py", line 519, in asolve
    final_args, final_kwargs, call = cast_gen.send(kwargs)
                                     ^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/core/model.py", line 274, in _solve
    casted_model = self.model(**solved_kw)
                   ^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/pydantic/main.py", line 171, in __init__
    self.__pydantic_validator__.validate_python(data, self_instance=self)
pydantic_core._pydantic_core.ValidationError: 1 validation error for update_feeds
msg
  Input should be a valid string [type=string_type, input_value={'item': {'id': 2, 'title...e': None}, 'feed_id': 1}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.6/v/string_type
2024-03-20 13:11:21,037 INFO     - product_feeds | product_feeds.feeds_update_requested    | 7d3f95fb-7 - Processed
2024-03-20 13:11:21,038 INFO     - product_feeds | product_feeds.one_feed_update_requested | e80925b4-c - Processing item; item_id=5 feed_id=1
2024-03-20 13:11:21,039 INFO     - product_feeds | product_feeds.one_feed_update_requested | e80925b4-c - Processing item; item_id=6 feed_id=1
2024-03-20 13:11:21,040 INFO     - product_feeds | product_feeds.one_feed_update_requested | e80925b4-c - Processing item; item_id=7 feed_id=1
2024-03-20 13:11:21,042 INFO     - product_feeds | product_feeds.one_feed_update_requested | e80925b4-c - Processing item; item_id=8 feed_id=1
2024-03-20 13:11:21,043 INFO     - product_feeds | product_feeds.one_feed_update_requested | e80925b4-c - Processing item; item_id=9 feed_id=1
2024-03-20 13:11:21,044 INFO     - product_feeds | product_feeds.one_feed_update_requested | e80925b4-c - Processing item; item_id=10 feed_id=1
2024-03-20 13:11:21,045 INFO     - product_feeds | product_feeds.one_feed_update_requested | e80925b4-c - Processing item; item_id=11 feed_id=1
2024-03-20 13:11:21,046 INFO     - product_feeds | product_feeds.one_feed_update_requested | e80925b4-c - Processing item; item_id=12 feed_id=1
2024-03-20 13:11:21,047 INFO     - product_feeds | product_feeds.one_feed_update_requested | e80925b4-c - Processing item; item_id=13 feed_id=1
2024-03-20 13:11:21,048 INFO     - product_feeds | product_feeds.one_feed_update_requested | e80925b4-c - Processing item; item_id=14 feed_id=1
2024-03-20 13:11:21,051 INFO     - product_feeds | product_feeds.one_feed_update_requested | e80925b4-c - Processing item; item_id=15 feed_id=1
2024-03-20 13:11:21,052 INFO     - product_feeds | product_feeds.one_feed_update_requested | e80925b4-c - Processing item; item_id=16 feed_id=1
2024-03-20 13:11:21,053 INFO     - product_feeds | product_feeds.one_feed_update_requested | e80925b4-c - Processing item; item_id=17 feed_id=1
2024-03-20 13:11:21,053 INFO     - product_feeds | product_feeds.one_feed_update_requested | e80925b4-c - Processing item; item_id=18 feed_id=1
2024-03-20 13:11:21,054 INFO     - product_feeds | product_feeds.one_feed_update_requested | e80925b4-c - Processing item; item_id=19 feed_id=1
2024-03-20 13:11:21,055 INFO     - product_feeds | product_feeds.one_feed_update_requested | e80925b4-c - Processing item; item_id=20 feed_id=1
2024-03-20 13:11:21,056 INFO     - product_feeds | product_feeds.one_feed_update_requested | e80925b4-c - Processing item; item_id=21 feed_id=1
2024-03-20 13:11:21,056 INFO     - product_feeds | product_feeds.one_feed_update_requested | e80925b4-c - Processing item; item_id=22 feed_id=1
2024-03-20 13:11:21,057 INFO     - product_feeds | product_feeds.one_feed_update_requested | e80925b4-c - Processing item; item_id=23 feed_id=1
2024-03-20 13:11:21,058 INFO     - product_feeds | product_feeds.one_feed_update_requested | e80925b4-c - Processing item; item_id=24 feed_id=1
2024-03-20 13:11:21,058 INFO     - product_feeds | product_feeds.one_feed_update_requested | e80925b4-c - Processing item; item_id=25 feed_id=1
2024-03-20 13:11:21,059 INFO     - product_feeds | product_feeds.one_feed_update_requested | e80925b4-c - Processing item; item_id=26 feed_id=1
2024-03-20 13:11:21,059 INFO     - product_feeds | product_feeds.one_feed_update_requested | e80925b4-c - Processing item; item_id=27 feed_id=1
2024-03-20 13:11:21,060 INFO     - product_feeds | product_feeds.one_feed_update_requested | e80925b4-c - Processing item; item_id=28 feed_id=1
2024-03-20 13:11:21,061 INFO     - product_feeds | product_feeds.one_feed_update_requested | e80925b4-c - Processing item; item_id=29 feed_id=1
2024-03-20 13:11:21,061 INFO     - product_feeds | product_feeds.one_feed_update_requested | e80925b4-c - Processing item; item_id=30 feed_id=1
2024-03-20 13:11:21,062 INFO     - product_feeds | product_feeds.one_feed_update_requested | e80925b4-c - Processing item; item_id=31 feed_id=1
2024-03-20 13:11:21,062 INFO     - product_feeds | product_feeds.one_feed_update_requested | e80925b4-c - Processing item; item_id=32 feed_id=1
2024-03-20 13:11:21,063 INFO     - product_feeds | product_feeds.one_feed_update_requested | e80925b4-c - Processing item; item_id=33 feed_id=1
2024-03-20 13:11:21,064 INFO     - product_feeds | product_feeds.one_feed_update_requested | e80925b4-c - Processing item; item_id=34 feed_id=1
2024-03-20 13:11:21,064 INFO     - product_feeds | product_feeds.one_feed_update_requested | e80925b4-c - Processing item; item_id=35 feed_id=1
2024-03-20 13:11:21,065 INFO     - product_feeds | product_feeds.one_feed_update_requested | e80925b4-c - Processing item; item_id=36 feed_id=1
2024-03-20 13:11:21,066 INFO     - product_feeds | product_feeds.one_feed_update_requested | e80925b4-c - Processing item; item_id=37 feed_id=1
2024-03-20 13:11:21,066 INFO     - product_feeds | product_feeds.one_feed_update_requested | e80925b4-c - Processing item; item_id=38 feed_id=1
2024-03-20 13:11:21,067 INFO     - product_feeds | product_feeds.one_feed_update_requested | e80925b4-c - Processing item; item_id=39 feed_id=1
2024-03-20 13:11:21,068 INFO     - product_feeds | product_feeds.one_feed_update_requested | e80925b4-c - Processing item; item_id=40 feed_id=1
2024-03-20 13:11:21,068 INFO     - product_feeds | product_feeds.one_feed_update_requested | e80925b4-c - Processing item; item_id=41 feed_id=1
2024-03-20 13:11:21,069 INFO     - product_feeds | product_feeds.one_feed_update_requested | e80925b4-c - Processing item; item_id=42 feed_id=1
2024-03-20 13:11:21,070 INFO     - product_feeds | product_feeds.one_feed_update_requested | e80925b4-c - Processing item; item_id=43 feed_id=1
2024-03-20 13:11:21,070 INFO     - product_feeds | product_feeds.one_feed_update_requested | e80925b4-c - Processing item; item_id=44 feed_id=1
2024-03-20 13:11:21,071 INFO     - product_feeds | product_feeds.one_feed_update_requested | e80925b4-c - Processing item; item_id=45 feed_id=1
2024-03-20 13:11:21,071 INFO     - product_feeds | product_feeds.one_feed_update_requested | e80925b4-c - Processing item; item_id=46 feed_id=1
2024-03-20 13:11:21,081 INFO     - product_feeds | product_feeds.one_feed_update_requested | e80925b4-c - Processing item; item_id=47 feed_id=1
2024-03-20 13:11:21,082 INFO     - product_feeds | product_feeds.one_feed_update_requested | e80925b4-c - Processing item; item_id=48 feed_id=1
2024-03-20 13:11:21,083 INFO     - product_feeds | product_feeds.one_feed_update_requested | e80925b4-c - Processing item; item_id=49 feed_id=1
2024-03-20 13:11:21,084 INFO     - product_feeds | product_feeds.one_feed_update_requested | e80925b4-c - Processing item; item_id=50 feed_id=1
2024-03-20 13:11:21,085 INFO     - product_feeds | product_feeds.one_feed_update_requested | e80925b4-c - Processing item; item_id=51 feed_id=1
2024-03-20 13:11:21,086 INFO     - product_feeds | product_feeds.one_feed_update_requested | e80925b4-c - Processing item; item_id=52 feed_id=1
2024-03-20 13:11:21,087 INFO     - product_feeds | product_feeds.one_feed_update_requested | e80925b4-c - Processing item; item_id=53 feed_id=1
2024-03-20 13:11:21,088 INFO     - product_feeds | product_feeds.one_feed_update_requested | e80925b4-c - Processing item; item_id=54 feed_id=1
2024-03-20 13:11:21,088 INFO     - product_feeds | product_feeds.one_feed_update_requested | e80925b4-c - Processing item; item_id=55 feed_id=1
2024-03-20 13:11:21,096 INFO     - product_feeds | product_feeds.one_feed_update_requested | e80925b4-c - Processing item; item_id=56 feed_id=1
2024-03-20 13:11:21,097 INFO     - product_feeds | product_feeds.one_feed_update_requested | e80925b4-c - Processing item; item_id=57 feed_id=1
2024-03-20 13:11:21,097 INFO     - product_feeds | product_feeds.one_feed_update_requested | e80925b4-c - Processing item; item_id=58 feed_id=1
2024-03-20 13:11:21,098 INFO     - product_feeds | product_feeds.one_feed_update_requested | e80925b4-c - Processing item; item_id=59 feed_id=1
2024-03-20 13:11:21,099 INFO     - product_feeds | product_feeds.one_feed_update_requested | e80925b4-c - Processing item; item_id=60 feed_id=1
2024-03-20 13:11:21,099 INFO     - product_feeds | product_feeds.one_feed_update_requested | e80925b4-c - Processing item; item_id=61 feed_id=1
2024-03-20 13:11:21,100 INFO     - product_feeds | product_feeds.one_feed_update_requested | e80925b4-c - Processing item; item_id=62 feed_id=1
2024-03-20 13:11:21,101 INFO     - product_feeds | product_feeds.one_feed_update_requested | e80925b4-c - Processing item; item_id=63 feed_id=1
2024-03-20 13:11:21,102 INFO     - product_feeds | product_feeds.one_feed_update_requested | e80925b4-c - Processing item; item_id=64 feed_id=1
2024-03-20 13:11:21,103 INFO     - product_feeds | product_feeds.one_feed_update_requested | e80925b4-c - Processing item; item_id=65 feed_id=1
2024-03-20 13:11:21,103 INFO     - product_feeds | product_feeds.one_feed_update_requested | e80925b4-c - Processing item; item_id=66 feed_id=1
2024-03-20 13:11:21,104 INFO     - product_feeds | product_feeds.one_feed_update_requested | e80925b4-c - Processing item; item_id=67 feed_id=1
2024-03-20 13:11:21,105 INFO     - product_feeds | product_feeds.one_feed_update_requested | e80925b4-c - Processing item; item_id=68 feed_id=1
2024-03-20 13:11:21,106 INFO     - product_feeds | product_feeds.one_feed_update_requested | e80925b4-c - Processing item; item_id=69 feed_id=1
2024-03-20 13:11:21,106 INFO     - product_feeds | product_feeds.one_feed_update_requested | e80925b4-c - Processing item; item_id=70 feed_id=1
2024-03-20 13:11:21,107 INFO     - product_feeds | product_feeds.one_feed_update_requested | e80925b4-c - Processing item; item_id=71 feed_id=1
2024-03-20 13:11:21,108 INFO     - product_feeds | product_feeds.one_feed_update_requested | e80925b4-c - Processing item; item_id=72 feed_id=1
2024-03-20 13:11:21,108 INFO     - product_feeds | product_feeds.one_feed_update_requested | e80925b4-c - Processing item; item_id=73 feed_id=1
2024-03-20 13:11:21,116 INFO     - product_feeds | product_feeds.one_feed_update_requested | e80925b4-c - Processing item; item_id=74 feed_id=1
2024-03-20 13:11:21,117 INFO     - product_feeds | product_feeds.one_feed_update_requested | e80925b4-c - Processing item; item_id=75 feed_id=1
2024-03-20 13:11:21,118 INFO     - product_feeds | product_feeds.one_feed_update_requested | e80925b4-c - Processing item; item_id=76 feed_id=1
2024-03-20 13:11:21,119 INFO     - product_feeds | product_feeds.one_feed_update_requested | e80925b4-c - Processing item; item_id=77 feed_id=1
2024-03-20 13:11:21,119 INFO     - product_feeds | product_feeds.one_feed_update_requested | e80925b4-c - Processing item; item_id=78 feed_id=1
2024-03-20 13:11:21,120 INFO     - product_feeds | product_feeds.one_feed_update_requested | e80925b4-c - Processing item; item_id=79 feed_id=1
2024-03-20 13:11:21,121 INFO     - product_feeds | product_feeds.one_feed_update_requested | e80925b4-c - Processing item; item_id=80 feed_id=1
2024-03-20 13:11:21,121 INFO     - product_feeds | product_feeds.one_feed_update_requested | e80925b4-c - Processing item; item_id=81 feed_id=1
2024-03-20 13:11:21,122 INFO     - product_feeds | product_feeds.one_feed_update_requested | e80925b4-c - Processing item; item_id=82 feed_id=1
2024-03-20 13:11:21,123 INFO     - product_feeds | product_feeds.one_feed_update_requested | e80925b4-c - Processing item; item_id=83 feed_id=1
2024-03-20 13:11:21,123 INFO     - product_feeds | product_feeds.one_feed_update_requested | e80925b4-c - Processing item; item_id=84 feed_id=1
2024-03-20 13:11:21,124 INFO     - product_feeds | product_feeds.one_feed_update_requested | e80925b4-c - Processing item; item_id=85 feed_id=1
2024-03-20 13:11:21,125 INFO     - product_feeds | product_feeds.one_feed_update_requested | e80925b4-c - Processing item; item_id=86 feed_id=1
2024-03-20 13:11:21,125 INFO     - product_feeds | product_feeds.one_feed_update_requested | e80925b4-c - Processing item; item_id=87 feed_id=1
2024-03-20 13:11:21,126 INFO     - product_feeds | product_feeds.one_feed_update_requested | e80925b4-c - Processing item; item_id=88 feed_id=1
2024-03-20 13:11:21,127 INFO     - product_feeds | product_feeds.one_feed_update_requested | e80925b4-c - Processing item; item_id=89 feed_id=1
2024-03-20 13:11:21,127 INFO     - product_feeds | product_feeds.one_feed_update_requested | e80925b4-c - Processing item; item_id=90 feed_id=1
2024-03-20 13:11:21,128 INFO     - product_feeds | product_feeds.one_feed_update_requested | e80925b4-c - Processing item; item_id=91 feed_id=1
2024-03-20 13:11:21,129 INFO     - product_feeds | product_feeds.one_feed_update_requested | e80925b4-c - Processing item; item_id=92 feed_id=1
2024-03-20 13:11:21,129 INFO     - product_feeds | product_feeds.one_feed_update_requested | e80925b4-c - Processing item; item_id=93 feed_id=1
2024-03-20 13:11:21,140 INFO     - product_feeds | product_feeds.one_feed_update_requested | e80925b4-c - Processing item; item_id=94 feed_id=1
2024-03-20 13:11:21,141 INFO     - product_feeds | product_feeds.one_feed_update_requested | e80925b4-c - Processing item; item_id=95 feed_id=1
2024-03-20 13:11:21,142 INFO     - product_feeds | product_feeds.one_feed_update_requested | e80925b4-c - Processing item; item_id=96 feed_id=1
2024-03-20 13:11:21,142 INFO     - product_feeds | product_feeds.one_feed_update_requested | e80925b4-c - Processing item; item_id=97 feed_id=1
2024-03-20 13:11:21,143 INFO     - product_feeds | product_feeds.one_feed_update_requested | e80925b4-c - Processing item; item_id=98 feed_id=1
2024-03-20 13:11:21,144 INFO     - product_feeds | product_feeds.one_feed_update_requested | e80925b4-c - Processing item; item_id=99 feed_id=1
2024-03-20 13:11:21,145 INFO     - product_feeds | product_feeds.one_feed_update_requested | e80925b4-c - Processing item; item_id=100 feed_id=1
2024-03-20 13:11:21,145 INFO     - product_feeds | product_feeds.one_feed_update_requested | e80925b4-c - Processing item; item_id=101 feed_id=1
2024-03-20 13:11:21,146 INFO     - product_feeds | product_feeds.one_feed_update_requested | e80925b4-c - Processing item; item_id=102 feed_id=1
2024-03-20 13:11:21,146 INFO     - product_feeds | product_feeds.one_feed_update_requested | e80925b4-c - Processing item; item_id=103 feed_id=1
2024-03-20 13:11:21,147 INFO     - product_feeds | product_feeds.one_feed_update_requested | e80925b4-c - Processing item; item_id=104 feed_id=1
2024-03-20 13:11:21,148 INFO     - product_feeds | product_feeds.one_feed_update_requested | e80925b4-c - Processing item; item_id=105 feed_id=1
2024-03-20 13:11:21,148 INFO     - product_feeds | product_feeds.one_feed_update_requested | e80925b4-c - Processing item; item_id=106 feed_id=1
2024-03-20 13:11:21,149 INFO     - product_feeds | product_feeds.one_feed_update_requested | e80925b4-c - Processing item; item_id=107 feed_id=1
2024-03-20 13:11:21,159 INFO     - product_feeds | product_feeds.one_feed_update_requested | e80925b4-c - Processing item; item_id=108 feed_id=1
2024-03-20 13:11:21,159 INFO     - product_feeds | product_feeds.one_feed_update_requested | e80925b4-c - Processing item; item_id=109 feed_id=1
2024-03-20 13:11:21,160 INFO     - product_feeds | product_feeds.one_feed_update_requested | e80925b4-c - Processing item; item_id=110 feed_id=1
2024-03-20 13:11:21,161 INFO     - product_feeds | product_feeds.one_feed_update_requested | e80925b4-c - Processing item; item_id=111 feed_id=1
2024-03-20 13:11:21,162 INFO     - product_feeds | product_feeds.one_feed_update_requested | e80925b4-c - Processing item; item_id=112 feed_id=1
2024-03-20 13:11:21,162 INFO     - product_feeds | product_feeds.one_feed_update_requested | e80925b4-c - Processing item; item_id=113 feed_id=1
2024-03-20 13:11:21,163 INFO     - product_feeds | product_feeds.one_feed_update_requested | e80925b4-c - Processing item; item_id=114 feed_id=1
2024-03-20 13:11:21,164 INFO     - product_feeds | product_feeds.one_feed_update_requested | e80925b4-c - Processing item; item_id=115 feed_id=1
2024-03-20 13:11:21,164 INFO     - product_feeds | product_feeds.one_feed_update_requested | e80925b4-c - Processing item; item_id=116 feed_id=1
2024-03-20 13:11:21,165 INFO     - product_feeds | product_feeds.one_feed_update_requested | e80925b4-c - Processing item; item_id=117 feed_id=1
2024-03-20 13:11:21,165 INFO     - product_feeds | product_feeds.one_feed_update_requested | e80925b4-c - Processing item; item_id=118 feed_id=1
2024-03-20 13:11:21,166 INFO     - product_feeds | product_feeds.one_feed_update_requested | e80925b4-c - Processing item; item_id=119 feed_id=1
2024-03-20 13:11:21,167 INFO     - product_feeds | product_feeds.one_feed_update_requested | e80925b4-c - Processing item; item_id=120 feed_id=1
2024-03-20 13:11:21,168 INFO     - product_feeds | product_feeds.one_feed_update_requested | e80925b4-c - Processing item; item_id=121 feed_id=1
2024-03-20 13:11:21,168 INFO     - product_feeds | product_feeds.one_feed_update_requested | e80925b4-c - Processing item; item_id=122 feed_id=1
2024-03-20 13:11:21,169 INFO     - product_feeds | product_feeds.one_feed_update_requested | e80925b4-c - Processing item; item_id=123 feed_id=1
2024-03-20 13:11:21,170 ERROR    - product_feeds | product_feeds.one_feed_update_requested | e80925b4-c - AttributeError: type object 'datetime.datetime' has no attribute 'datetime'
Traceback (most recent call last):
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/handler.py", line 367, in consume
    raise e
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/handler.py", line 331, in consume
    result = await cast(
             ^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/utils.py", line 95, in set_message_wrapper
    return await func(message)
           ^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/nats/broker.py", line 244, in process_wrapper
    r = await func(message)
        ^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/core/asynchronous.py", line 406, in decode_wrapper
    return await func(msg)
           ^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/use.py", line 146, in injected_wrapper
    r = await real_model.asolve(
        ^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/core/model.py", line 529, in asolve
    response = await run_async(call, *final_args, **final_kwargs)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/utils.py", line 48, in run_async
    return await cast(Callable[P, Awaitable[T]], func)(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/utils/functions.py", line 90, in to_async_wrapper
    return await call_or_await(func, *args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/utils.py", line 48, in run_async
    return await cast(Callable[P, Awaitable[T]], func)(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/stream/handlers.py", line 95, in update_feed
    started_at=datetime.datetime.now(),
               ^^^^^^^^^^^^^^^^^
AttributeError: type object 'datetime.datetime' has no attribute 'datetime'
2024-03-20 13:11:21,178 INFO     - product_feeds | product_feeds.one_feed_update_requested | e80925b4-c - Processed
2024-03-20 13:11:21,180 INFO     - product_feeds | product_feeds.one_feed_update_requested | eef54466-1 - Received
2024-03-20 13:11:21,180 INFO     - product_feeds | product_feeds.one_feed_update_requested | 263fd374-a - Received
2024-03-20 13:11:21,181 INFO     - product_feeds | product_feeds.one_feed_update_requested | 266ce607-9 - Received
2024-03-20 13:11:21,181 INFO     - product_feeds | product_feeds.one_feed_update_requested | 7ac399b5-b - Received
2024-03-20 13:11:21,181 INFO     - product_feeds | product_feeds.one_feed_update_requested | bb688fe2-3 - Received
2024-03-20 13:11:21,181 INFO     - product_feeds | product_feeds.one_feed_update_requested | fc2616aa-1 - Received
2024-03-20 13:11:21,181 INFO     - product_feeds | product_feeds.one_feed_update_requested | 2d97ff5c-3 - Received
2024-03-20 13:11:21,181 INFO     - product_feeds | product_feeds.one_feed_update_requested | 7bcf4b65-5 - Received
2024-03-20 13:11:21,181 INFO     - product_feeds | product_feeds.one_feed_update_requested | 22b944f3-1 - Received
2024-03-20 13:11:21,181 INFO     - product_feeds | product_feeds.one_feed_update_requested | 362335d7-6 - Received
2024-03-20 13:11:21,184 ERROR    - product_feeds | product_feeds.one_feed_update_requested | eef54466-1 - ValidationError: 1 validation error for update_feed
feed_id
  Input should be a valid integer [type=int_type, input_value={'item': {'id': 6, 'title...e': None}, 'feed_id': 1}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.6/v/int_type
Traceback (most recent call last):
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/handler.py", line 367, in consume
    raise e
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/handler.py", line 331, in consume
    result = await cast(
             ^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/utils.py", line 95, in set_message_wrapper
    return await func(message)
           ^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/nats/broker.py", line 244, in process_wrapper
    r = await func(message)
        ^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/core/asynchronous.py", line 406, in decode_wrapper
    return await func(msg)
           ^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/use.py", line 146, in injected_wrapper
    r = await real_model.asolve(
        ^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/core/model.py", line 519, in asolve
    final_args, final_kwargs, call = cast_gen.send(kwargs)
                                     ^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/core/model.py", line 274, in _solve
    casted_model = self.model(**solved_kw)
                   ^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/pydantic/main.py", line 171, in __init__
    self.__pydantic_validator__.validate_python(data, self_instance=self)
pydantic_core._pydantic_core.ValidationError: 1 validation error for update_feed
feed_id
  Input should be a valid integer [type=int_type, input_value={'item': {'id': 6, 'title...e': None}, 'feed_id': 1}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.6/v/int_type
2024-03-20 13:11:21,185 INFO     - product_feeds | product_feeds.one_feed_update_requested | eef54466-1 - Processed
2024-03-20 13:11:21,185 ERROR    - product_feeds | product_feeds.one_feed_update_requested | 266ce607-9 - ValidationError: 1 validation error for update_feed
feed_id
  Input should be a valid integer [type=int_type, input_value={'item': {'id': 8, 'title...e': None}, 'feed_id': 1}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.6/v/int_type
Traceback (most recent call last):
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/handler.py", line 367, in consume
    raise e
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/handler.py", line 331, in consume
    result = await cast(
             ^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/utils.py", line 95, in set_message_wrapper
    return await func(message)
           ^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/nats/broker.py", line 244, in process_wrapper
    r = await func(message)
        ^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/core/asynchronous.py", line 406, in decode_wrapper
    return await func(msg)
           ^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/use.py", line 146, in injected_wrapper
    r = await real_model.asolve(
        ^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/core/model.py", line 519, in asolve
    final_args, final_kwargs, call = cast_gen.send(kwargs)
                                     ^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/core/model.py", line 274, in _solve
    casted_model = self.model(**solved_kw)
                   ^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/pydantic/main.py", line 171, in __init__
    self.__pydantic_validator__.validate_python(data, self_instance=self)
pydantic_core._pydantic_core.ValidationError: 1 validation error for update_feed
feed_id
  Input should be a valid integer [type=int_type, input_value={'item': {'id': 8, 'title...e': None}, 'feed_id': 1}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.6/v/int_type
2024-03-20 13:11:21,186 INFO     - product_feeds | product_feeds.one_feed_update_requested | 266ce607-9 - Processed
2024-03-20 13:11:21,186 ERROR    - product_feeds | product_feeds.one_feed_update_requested | bb688fe2-3 - ValidationError: 1 validation error for update_feed
feed_id
  Input should be a valid integer [type=int_type, input_value={'item': {'id': 10, 'titl...e': None}, 'feed_id': 1}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.6/v/int_type
Traceback (most recent call last):
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/handler.py", line 367, in consume
    raise e
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/handler.py", line 331, in consume
    result = await cast(
             ^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/utils.py", line 95, in set_message_wrapper
    return await func(message)
           ^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/nats/broker.py", line 244, in process_wrapper
    r = await func(message)
        ^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/core/asynchronous.py", line 406, in decode_wrapper
    return await func(msg)
           ^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/use.py", line 146, in injected_wrapper
    r = await real_model.asolve(
        ^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/core/model.py", line 519, in asolve
    final_args, final_kwargs, call = cast_gen.send(kwargs)
                                     ^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/core/model.py", line 274, in _solve
    casted_model = self.model(**solved_kw)
                   ^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/pydantic/main.py", line 171, in __init__
    self.__pydantic_validator__.validate_python(data, self_instance=self)
pydantic_core._pydantic_core.ValidationError: 1 validation error for update_feed
feed_id
  Input should be a valid integer [type=int_type, input_value={'item': {'id': 10, 'titl...e': None}, 'feed_id': 1}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.6/v/int_type
2024-03-20 13:11:21,194 INFO     - product_feeds | product_feeds.one_feed_update_requested | bb688fe2-3 - Processed
2024-03-20 13:11:21,194 ERROR    - product_feeds | product_feeds.one_feed_update_requested | 22b944f3-1 - ValidationError: 1 validation error for update_feed
feed_id
  Input should be a valid integer [type=int_type, input_value={'item': {'id': 14, 'titl...e': None}, 'feed_id': 1}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.6/v/int_type
Traceback (most recent call last):
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/handler.py", line 367, in consume
    raise e
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/handler.py", line 331, in consume
    result = await cast(
             ^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/utils.py", line 95, in set_message_wrapper
    return await func(message)
           ^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/nats/broker.py", line 244, in process_wrapper
    r = await func(message)
        ^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/core/asynchronous.py", line 406, in decode_wrapper
    return await func(msg)
           ^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/use.py", line 146, in injected_wrapper
    r = await real_model.asolve(
        ^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/core/model.py", line 519, in asolve
    final_args, final_kwargs, call = cast_gen.send(kwargs)
                                     ^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/core/model.py", line 274, in _solve
    casted_model = self.model(**solved_kw)
                   ^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/pydantic/main.py", line 171, in __init__
    self.__pydantic_validator__.validate_python(data, self_instance=self)
pydantic_core._pydantic_core.ValidationError: 1 validation error for update_feed
feed_id
  Input should be a valid integer [type=int_type, input_value={'item': {'id': 14, 'titl...e': None}, 'feed_id': 1}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.6/v/int_type
2024-03-20 13:11:21,195 INFO     - product_feeds | product_feeds.one_feed_update_requested | 22b944f3-1 - Processed
2024-03-20 13:11:21,195 ERROR    - product_feeds | product_feeds.one_feed_update_requested | 362335d7-6 - ValidationError: 1 validation error for update_feed
feed_id
  Input should be a valid integer [type=int_type, input_value={'item': {'id': 15, 'titl...e': None}, 'feed_id': 1}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.6/v/int_type
Traceback (most recent call last):
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/handler.py", line 367, in consume
    raise e
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/handler.py", line 331, in consume
    result = await cast(
             ^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/utils.py", line 95, in set_message_wrapper
    return await func(message)
           ^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/nats/broker.py", line 244, in process_wrapper
    r = await func(message)
        ^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/core/asynchronous.py", line 406, in decode_wrapper
    return await func(msg)
           ^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/use.py", line 146, in injected_wrapper
    r = await real_model.asolve(
        ^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/core/model.py", line 519, in asolve
    final_args, final_kwargs, call = cast_gen.send(kwargs)
                                     ^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/core/model.py", line 274, in _solve
    casted_model = self.model(**solved_kw)
                   ^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/pydantic/main.py", line 171, in __init__
    self.__pydantic_validator__.validate_python(data, self_instance=self)
pydantic_core._pydantic_core.ValidationError: 1 validation error for update_feed
feed_id
  Input should be a valid integer [type=int_type, input_value={'item': {'id': 15, 'titl...e': None}, 'feed_id': 1}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.6/v/int_type
2024-03-20 13:11:21,196 INFO     - product_feeds | product_feeds.one_feed_update_requested | 362335d7-6 - Processed
2024-03-20 13:11:21,196 ERROR    - product_feeds | product_feeds.one_feed_update_requested | 263fd374-a - ValidationError: 1 validation error for update_feed
feed_id
  Input should be a valid integer [type=int_type, input_value={'item': {'id': 7, 'title...e': None}, 'feed_id': 1}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.6/v/int_type
Traceback (most recent call last):
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/handler.py", line 367, in consume
    raise e
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/handler.py", line 331, in consume
    result = await cast(
             ^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/utils.py", line 95, in set_message_wrapper
    return await func(message)
           ^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/nats/broker.py", line 244, in process_wrapper
    r = await func(message)
        ^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/core/asynchronous.py", line 406, in decode_wrapper
    return await func(msg)
           ^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/use.py", line 146, in injected_wrapper
    r = await real_model.asolve(
        ^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/core/model.py", line 519, in asolve
    final_args, final_kwargs, call = cast_gen.send(kwargs)
                                     ^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/core/model.py", line 274, in _solve
    casted_model = self.model(**solved_kw)
                   ^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/pydantic/main.py", line 171, in __init__
    self.__pydantic_validator__.validate_python(data, self_instance=self)
pydantic_core._pydantic_core.ValidationError: 1 validation error for update_feed
feed_id
  Input should be a valid integer [type=int_type, input_value={'item': {'id': 7, 'title...e': None}, 'feed_id': 1}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.6/v/int_type
2024-03-20 13:11:21,197 INFO     - product_feeds | product_feeds.one_feed_update_requested | 263fd374-a - Processed
2024-03-20 13:11:21,197 ERROR    - product_feeds | product_feeds.one_feed_update_requested | 2d97ff5c-3 - ValidationError: 1 validation error for update_feed
feed_id
  Input should be a valid integer [type=int_type, input_value={'item': {'id': 12, 'titl...e': None}, 'feed_id': 1}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.6/v/int_type
Traceback (most recent call last):
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/handler.py", line 367, in consume
    raise e
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/handler.py", line 331, in consume
    result = await cast(
             ^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/utils.py", line 95, in set_message_wrapper
    return await func(message)
           ^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/nats/broker.py", line 244, in process_wrapper
    r = await func(message)
        ^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/core/asynchronous.py", line 406, in decode_wrapper
    return await func(msg)
           ^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/use.py", line 146, in injected_wrapper
    r = await real_model.asolve(
        ^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/core/model.py", line 519, in asolve
    final_args, final_kwargs, call = cast_gen.send(kwargs)
                                     ^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/core/model.py", line 274, in _solve
    casted_model = self.model(**solved_kw)
                   ^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/pydantic/main.py", line 171, in __init__
    self.__pydantic_validator__.validate_python(data, self_instance=self)
pydantic_core._pydantic_core.ValidationError: 1 validation error for update_feed
feed_id
  Input should be a valid integer [type=int_type, input_value={'item': {'id': 12, 'titl...e': None}, 'feed_id': 1}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.6/v/int_type
2024-03-20 13:11:21,198 INFO     - product_feeds | product_feeds.one_feed_update_requested | 2d97ff5c-3 - Processed
2024-03-20 13:11:21,198 ERROR    - product_feeds | product_feeds.one_feed_update_requested | 7ac399b5-b - ValidationError: 1 validation error for update_feed
feed_id
  Input should be a valid integer [type=int_type, input_value={'item': {'id': 9, 'title...e': None}, 'feed_id': 1}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.6/v/int_type
Traceback (most recent call last):
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/handler.py", line 367, in consume
    raise e
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/handler.py", line 331, in consume
    result = await cast(
             ^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/utils.py", line 95, in set_message_wrapper
    return await func(message)
           ^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/nats/broker.py", line 244, in process_wrapper
    r = await func(message)
        ^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/core/asynchronous.py", line 406, in decode_wrapper
    return await func(msg)
           ^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/use.py", line 146, in injected_wrapper
    r = await real_model.asolve(
        ^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/core/model.py", line 519, in asolve
    final_args, final_kwargs, call = cast_gen.send(kwargs)
                                     ^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/core/model.py", line 274, in _solve
    casted_model = self.model(**solved_kw)
                   ^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/pydantic/main.py", line 171, in __init__
    self.__pydantic_validator__.validate_python(data, self_instance=self)
pydantic_core._pydantic_core.ValidationError: 1 validation error for update_feed
feed_id
  Input should be a valid integer [type=int_type, input_value={'item': {'id': 9, 'title...e': None}, 'feed_id': 1}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.6/v/int_type
2024-03-20 13:11:21,199 INFO     - product_feeds | product_feeds.one_feed_update_requested | 7ac399b5-b - Processed
2024-03-20 13:11:21,199 ERROR    - product_feeds | product_feeds.one_feed_update_requested | fc2616aa-1 - ValidationError: 1 validation error for update_feed
feed_id
  Input should be a valid integer [type=int_type, input_value={'item': {'id': 11, 'titl...e': None}, 'feed_id': 1}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.6/v/int_type
Traceback (most recent call last):
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/handler.py", line 367, in consume
    raise e
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/handler.py", line 331, in consume
    result = await cast(
             ^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/utils.py", line 95, in set_message_wrapper
    return await func(message)
           ^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/nats/broker.py", line 244, in process_wrapper
    r = await func(message)
        ^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/core/asynchronous.py", line 406, in decode_wrapper
    return await func(msg)
           ^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/use.py", line 146, in injected_wrapper
    r = await real_model.asolve(
        ^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/core/model.py", line 519, in asolve
    final_args, final_kwargs, call = cast_gen.send(kwargs)
                                     ^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/core/model.py", line 274, in _solve
    casted_model = self.model(**solved_kw)
                   ^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/pydantic/main.py", line 171, in __init__
    self.__pydantic_validator__.validate_python(data, self_instance=self)
pydantic_core._pydantic_core.ValidationError: 1 validation error for update_feed
feed_id
  Input should be a valid integer [type=int_type, input_value={'item': {'id': 11, 'titl...e': None}, 'feed_id': 1}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.6/v/int_type
2024-03-20 13:11:21,200 INFO     - product_feeds | product_feeds.one_feed_update_requested | fc2616aa-1 - Processed
2024-03-20 13:11:21,200 ERROR    - product_feeds | product_feeds.one_feed_update_requested | 7bcf4b65-5 - ValidationError: 1 validation error for update_feed
feed_id
  Input should be a valid integer [type=int_type, input_value={'item': {'id': 13, 'titl...e': None}, 'feed_id': 1}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.6/v/int_type
Traceback (most recent call last):
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/handler.py", line 367, in consume
    raise e
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/handler.py", line 331, in consume
    result = await cast(
             ^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/utils.py", line 95, in set_message_wrapper
    return await func(message)
           ^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/nats/broker.py", line 244, in process_wrapper
    r = await func(message)
        ^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/core/asynchronous.py", line 406, in decode_wrapper
    return await func(msg)
           ^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/use.py", line 146, in injected_wrapper
    r = await real_model.asolve(
        ^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/core/model.py", line 519, in asolve
    final_args, final_kwargs, call = cast_gen.send(kwargs)
                                     ^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/core/model.py", line 274, in _solve
    casted_model = self.model(**solved_kw)
                   ^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/pydantic/main.py", line 171, in __init__
    self.__pydantic_validator__.validate_python(data, self_instance=self)
pydantic_core._pydantic_core.ValidationError: 1 validation error for update_feed
feed_id
  Input should be a valid integer [type=int_type, input_value={'item': {'id': 13, 'titl...e': None}, 'feed_id': 1}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.6/v/int_type
2024-03-20 13:11:21,201 INFO     - product_feeds | product_feeds.one_feed_update_requested | 7bcf4b65-5 - Processed
2024-03-20 13:11:21,203 INFO     - product_feeds | product_feeds.one_feed_update_requested | 7246e62c-8 - Received
2024-03-20 13:11:21,204 INFO     - product_feeds | product_feeds.one_feed_update_requested | 46bb2a9c-c - Received
2024-03-20 13:11:21,204 INFO     - product_feeds | product_feeds.one_feed_update_requested | c156279b-9 - Received
2024-03-20 13:11:21,204 INFO     - product_feeds | product_feeds.one_feed_update_requested | c02edd97-7 - Received
2024-03-20 13:11:21,204 INFO     - product_feeds | product_feeds.one_feed_update_requested | 50f01367-9 - Received
2024-03-20 13:11:21,204 INFO     - product_feeds | product_feeds.one_feed_update_requested | d40e2f84-1 - Received
2024-03-20 13:11:21,204 INFO     - product_feeds | product_feeds.one_feed_update_requested | e72ed0f4-0 - Received
2024-03-20 13:11:21,204 INFO     - product_feeds | product_feeds.one_feed_update_requested | 36063bc3-8 - Received
2024-03-20 13:11:21,204 INFO     - product_feeds | product_feeds.one_feed_update_requested | 1486ada5-8 - Received
2024-03-20 13:11:21,204 INFO     - product_feeds | product_feeds.one_feed_update_requested | 30dbd43b-1 - Received
2024-03-20 13:11:21,206 ERROR    - product_feeds | product_feeds.one_feed_update_requested | d40e2f84-1 - ValidationError: 1 validation error for update_feed
feed_id
  Input should be a valid integer [type=int_type, input_value={'item': {'id': 21, 'titl...e': None}, 'feed_id': 1}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.6/v/int_type
Traceback (most recent call last):
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/handler.py", line 367, in consume
    raise e
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/handler.py", line 331, in consume
    result = await cast(
             ^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/utils.py", line 95, in set_message_wrapper
    return await func(message)
           ^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/nats/broker.py", line 244, in process_wrapper
    r = await func(message)
        ^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/core/asynchronous.py", line 406, in decode_wrapper
    return await func(msg)
           ^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/use.py", line 146, in injected_wrapper
    r = await real_model.asolve(
        ^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/core/model.py", line 519, in asolve
    final_args, final_kwargs, call = cast_gen.send(kwargs)
                                     ^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/core/model.py", line 274, in _solve
    casted_model = self.model(**solved_kw)
                   ^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/pydantic/main.py", line 171, in __init__
    self.__pydantic_validator__.validate_python(data, self_instance=self)
pydantic_core._pydantic_core.ValidationError: 1 validation error for update_feed
feed_id
  Input should be a valid integer [type=int_type, input_value={'item': {'id': 21, 'titl...e': None}, 'feed_id': 1}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.6/v/int_type
2024-03-20 13:11:21,215 INFO     - product_feeds | product_feeds.one_feed_update_requested | d40e2f84-1 - Processed
2024-03-20 13:11:21,215 ERROR    - product_feeds | product_feeds.one_feed_update_requested | 36063bc3-8 - ValidationError: 1 validation error for update_feed
feed_id
  Input should be a valid integer [type=int_type, input_value={'item': {'id': 23, 'titl...e': None}, 'feed_id': 1}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.6/v/int_type
Traceback (most recent call last):
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/handler.py", line 367, in consume
    raise e
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/handler.py", line 331, in consume
    result = await cast(
             ^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/utils.py", line 95, in set_message_wrapper
    return await func(message)
           ^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/nats/broker.py", line 244, in process_wrapper
    r = await func(message)
        ^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/core/asynchronous.py", line 406, in decode_wrapper
    return await func(msg)
           ^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/use.py", line 146, in injected_wrapper
    r = await real_model.asolve(
        ^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/core/model.py", line 519, in asolve
    final_args, final_kwargs, call = cast_gen.send(kwargs)
                                     ^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/core/model.py", line 274, in _solve
    casted_model = self.model(**solved_kw)
                   ^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/pydantic/main.py", line 171, in __init__
    self.__pydantic_validator__.validate_python(data, self_instance=self)
pydantic_core._pydantic_core.ValidationError: 1 validation error for update_feed
feed_id
  Input should be a valid integer [type=int_type, input_value={'item': {'id': 23, 'titl...e': None}, 'feed_id': 1}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.6/v/int_type
2024-03-20 13:11:21,216 INFO     - product_feeds | product_feeds.one_feed_update_requested | 36063bc3-8 - Processed
2024-03-20 13:11:21,216 ERROR    - product_feeds | product_feeds.one_feed_update_requested | 50f01367-9 - ValidationError: 1 validation error for update_feed
feed_id
  Input should be a valid integer [type=int_type, input_value={'item': {'id': 20, 'titl...e': None}, 'feed_id': 1}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.6/v/int_type
Traceback (most recent call last):
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/handler.py", line 367, in consume
    raise e
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/handler.py", line 331, in consume
    result = await cast(
             ^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/utils.py", line 95, in set_message_wrapper
    return await func(message)
           ^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/nats/broker.py", line 244, in process_wrapper
    r = await func(message)
        ^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/core/asynchronous.py", line 406, in decode_wrapper
    return await func(msg)
           ^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/use.py", line 146, in injected_wrapper
    r = await real_model.asolve(
        ^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/core/model.py", line 519, in asolve
    final_args, final_kwargs, call = cast_gen.send(kwargs)
                                     ^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/core/model.py", line 274, in _solve
    casted_model = self.model(**solved_kw)
                   ^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/pydantic/main.py", line 171, in __init__
    self.__pydantic_validator__.validate_python(data, self_instance=self)
pydantic_core._pydantic_core.ValidationError: 1 validation error for update_feed
feed_id
  Input should be a valid integer [type=int_type, input_value={'item': {'id': 20, 'titl...e': None}, 'feed_id': 1}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.6/v/int_type
2024-03-20 13:11:21,217 INFO     - product_feeds | product_feeds.one_feed_update_requested | 50f01367-9 - Processed
2024-03-20 13:11:21,217 ERROR    - product_feeds | product_feeds.one_feed_update_requested | 7246e62c-8 - ValidationError: 1 validation error for update_feed
feed_id
  Input should be a valid integer [type=int_type, input_value={'item': {'id': 16, 'titl...e': None}, 'feed_id': 1}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.6/v/int_type
Traceback (most recent call last):
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/handler.py", line 367, in consume
    raise e
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/handler.py", line 331, in consume
    result = await cast(
             ^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/utils.py", line 95, in set_message_wrapper
    return await func(message)
           ^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/nats/broker.py", line 244, in process_wrapper
    r = await func(message)
        ^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/core/asynchronous.py", line 406, in decode_wrapper
    return await func(msg)
           ^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/use.py", line 146, in injected_wrapper
    r = await real_model.asolve(
        ^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/core/model.py", line 519, in asolve
    final_args, final_kwargs, call = cast_gen.send(kwargs)
                                     ^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/core/model.py", line 274, in _solve
    casted_model = self.model(**solved_kw)
                   ^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/pydantic/main.py", line 171, in __init__
    self.__pydantic_validator__.validate_python(data, self_instance=self)
pydantic_core._pydantic_core.ValidationError: 1 validation error for update_feed
feed_id
  Input should be a valid integer [type=int_type, input_value={'item': {'id': 16, 'titl...e': None}, 'feed_id': 1}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.6/v/int_type
2024-03-20 13:11:21,218 INFO     - product_feeds | product_feeds.one_feed_update_requested | 7246e62c-8 - Processed
2024-03-20 13:11:21,218 ERROR    - product_feeds | product_feeds.one_feed_update_requested | e72ed0f4-0 - ValidationError: 1 validation error for update_feed
feed_id
  Input should be a valid integer [type=int_type, input_value={'item': {'id': 22, 'titl...e': None}, 'feed_id': 1}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.6/v/int_type
Traceback (most recent call last):
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/handler.py", line 367, in consume
    raise e
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/handler.py", line 331, in consume
    result = await cast(
             ^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/utils.py", line 95, in set_message_wrapper
    return await func(message)
           ^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/nats/broker.py", line 244, in process_wrapper
    r = await func(message)
        ^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/core/asynchronous.py", line 406, in decode_wrapper
    return await func(msg)
           ^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/use.py", line 146, in injected_wrapper
    r = await real_model.asolve(
        ^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/core/model.py", line 519, in asolve
    final_args, final_kwargs, call = cast_gen.send(kwargs)
                                     ^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/core/model.py", line 274, in _solve
    casted_model = self.model(**solved_kw)
                   ^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/pydantic/main.py", line 171, in __init__
    self.__pydantic_validator__.validate_python(data, self_instance=self)
pydantic_core._pydantic_core.ValidationError: 1 validation error for update_feed
feed_id
  Input should be a valid integer [type=int_type, input_value={'item': {'id': 22, 'titl...e': None}, 'feed_id': 1}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.6/v/int_type
2024-03-20 13:11:21,219 INFO     - product_feeds | product_feeds.one_feed_update_requested | e72ed0f4-0 - Processed
2024-03-20 13:11:21,219 ERROR    - product_feeds | product_feeds.one_feed_update_requested | c156279b-9 - ValidationError: 1 validation error for update_feed
feed_id
  Input should be a valid integer [type=int_type, input_value={'item': {'id': 18, 'titl...e': None}, 'feed_id': 1}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.6/v/int_type
Traceback (most recent call last):
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/handler.py", line 367, in consume
    raise e
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/handler.py", line 331, in consume
    result = await cast(
             ^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/utils.py", line 95, in set_message_wrapper
    return await func(message)
           ^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/nats/broker.py", line 244, in process_wrapper
    r = await func(message)
        ^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/core/asynchronous.py", line 406, in decode_wrapper
    return await func(msg)
           ^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/use.py", line 146, in injected_wrapper
    r = await real_model.asolve(
        ^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/core/model.py", line 519, in asolve
    final_args, final_kwargs, call = cast_gen.send(kwargs)
                                     ^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/core/model.py", line 274, in _solve
    casted_model = self.model(**solved_kw)
                   ^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/pydantic/main.py", line 171, in __init__
    self.__pydantic_validator__.validate_python(data, self_instance=self)
pydantic_core._pydantic_core.ValidationError: 1 validation error for update_feed
feed_id
  Input should be a valid integer [type=int_type, input_value={'item': {'id': 18, 'titl...e': None}, 'feed_id': 1}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.6/v/int_type
2024-03-20 13:11:21,220 INFO     - product_feeds | product_feeds.one_feed_update_requested | c156279b-9 - Processed
2024-03-20 13:11:21,220 ERROR    - product_feeds | product_feeds.one_feed_update_requested | 1486ada5-8 - ValidationError: 1 validation error for update_feed
feed_id
  Input should be a valid integer [type=int_type, input_value={'item': {'id': 24, 'titl...e': None}, 'feed_id': 1}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.6/v/int_type
Traceback (most recent call last):
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/handler.py", line 367, in consume
    raise e
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/handler.py", line 331, in consume
    result = await cast(
             ^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/utils.py", line 95, in set_message_wrapper
    return await func(message)
           ^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/nats/broker.py", line 244, in process_wrapper
    r = await func(message)
        ^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/core/asynchronous.py", line 406, in decode_wrapper
    return await func(msg)
           ^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/use.py", line 146, in injected_wrapper
    r = await real_model.asolve(
        ^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/core/model.py", line 519, in asolve
    final_args, final_kwargs, call = cast_gen.send(kwargs)
                                     ^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/core/model.py", line 274, in _solve
    casted_model = self.model(**solved_kw)
                   ^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/pydantic/main.py", line 171, in __init__
    self.__pydantic_validator__.validate_python(data, self_instance=self)
pydantic_core._pydantic_core.ValidationError: 1 validation error for update_feed
feed_id
  Input should be a valid integer [type=int_type, input_value={'item': {'id': 24, 'titl...e': None}, 'feed_id': 1}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.6/v/int_type
2024-03-20 13:11:21,221 INFO     - product_feeds | product_feeds.one_feed_update_requested | 1486ada5-8 - Processed
2024-03-20 13:11:21,221 ERROR    - product_feeds | product_feeds.one_feed_update_requested | 46bb2a9c-c - ValidationError: 1 validation error for update_feed
feed_id
  Input should be a valid integer [type=int_type, input_value={'item': {'id': 17, 'titl...e': None}, 'feed_id': 1}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.6/v/int_type
Traceback (most recent call last):
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/handler.py", line 367, in consume
    raise e
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/handler.py", line 331, in consume
    result = await cast(
             ^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/utils.py", line 95, in set_message_wrapper
    return await func(message)
           ^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/nats/broker.py", line 244, in process_wrapper
    r = await func(message)
        ^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/core/asynchronous.py", line 406, in decode_wrapper
    return await func(msg)
           ^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/use.py", line 146, in injected_wrapper
    r = await real_model.asolve(
        ^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/core/model.py", line 519, in asolve
    final_args, final_kwargs, call = cast_gen.send(kwargs)
                                     ^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/core/model.py", line 274, in _solve
    casted_model = self.model(**solved_kw)
                   ^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/pydantic/main.py", line 171, in __init__
    self.__pydantic_validator__.validate_python(data, self_instance=self)
pydantic_core._pydantic_core.ValidationError: 1 validation error for update_feed
feed_id
  Input should be a valid integer [type=int_type, input_value={'item': {'id': 17, 'titl...e': None}, 'feed_id': 1}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.6/v/int_type
2024-03-20 13:11:21,222 INFO     - product_feeds | product_feeds.one_feed_update_requested | 46bb2a9c-c - Processed
2024-03-20 13:11:21,222 ERROR    - product_feeds | product_feeds.one_feed_update_requested | 30dbd43b-1 - ValidationError: 1 validation error for update_feed
feed_id
  Input should be a valid integer [type=int_type, input_value={'item': {'id': 25, 'titl...e': None}, 'feed_id': 1}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.6/v/int_type
Traceback (most recent call last):
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/handler.py", line 367, in consume
    raise e
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/handler.py", line 331, in consume
    result = await cast(
             ^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/utils.py", line 95, in set_message_wrapper
    return await func(message)
           ^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/nats/broker.py", line 244, in process_wrapper
    r = await func(message)
        ^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/core/asynchronous.py", line 406, in decode_wrapper
    return await func(msg)
           ^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/use.py", line 146, in injected_wrapper
    r = await real_model.asolve(
        ^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/core/model.py", line 519, in asolve
    final_args, final_kwargs, call = cast_gen.send(kwargs)
                                     ^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/core/model.py", line 274, in _solve
    casted_model = self.model(**solved_kw)
                   ^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/pydantic/main.py", line 171, in __init__
    self.__pydantic_validator__.validate_python(data, self_instance=self)
pydantic_core._pydantic_core.ValidationError: 1 validation error for update_feed
feed_id
  Input should be a valid integer [type=int_type, input_value={'item': {'id': 25, 'titl...e': None}, 'feed_id': 1}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.6/v/int_type
2024-03-20 13:11:21,223 INFO     - product_feeds | product_feeds.one_feed_update_requested | 30dbd43b-1 - Processed
2024-03-20 13:11:21,223 ERROR    - product_feeds | product_feeds.one_feed_update_requested | c02edd97-7 - ValidationError: 1 validation error for update_feed
feed_id
  Input should be a valid integer [type=int_type, input_value={'item': {'id': 19, 'titl...e': None}, 'feed_id': 1}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.6/v/int_type
Traceback (most recent call last):
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/handler.py", line 367, in consume
    raise e
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/handler.py", line 331, in consume
    result = await cast(
             ^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/utils.py", line 95, in set_message_wrapper
    return await func(message)
           ^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/nats/broker.py", line 244, in process_wrapper
    r = await func(message)
        ^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/core/asynchronous.py", line 406, in decode_wrapper
    return await func(msg)
           ^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/use.py", line 146, in injected_wrapper
    r = await real_model.asolve(
        ^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/core/model.py", line 519, in asolve
    final_args, final_kwargs, call = cast_gen.send(kwargs)
                                     ^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/core/model.py", line 274, in _solve
    casted_model = self.model(**solved_kw)
                   ^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/pydantic/main.py", line 171, in __init__
    self.__pydantic_validator__.validate_python(data, self_instance=self)
pydantic_core._pydantic_core.ValidationError: 1 validation error for update_feed
feed_id
  Input should be a valid integer [type=int_type, input_value={'item': {'id': 19, 'titl...e': None}, 'feed_id': 1}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.6/v/int_type
2024-03-20 13:11:21,224 INFO     - product_feeds | product_feeds.one_feed_update_requested | c02edd97-7 - Processed
2024-03-20 13:11:21,226 INFO     - product_feeds | product_feeds.one_feed_update_requested | 1521f974-7 - Received
2024-03-20 13:11:21,226 INFO     - product_feeds | product_feeds.one_feed_update_requested | 7fbcc7cf-c - Received
2024-03-20 13:11:21,226 INFO     - product_feeds | product_feeds.one_feed_update_requested | d13c8f2b-d - Received
2024-03-20 13:11:21,226 INFO     - product_feeds | product_feeds.one_feed_update_requested | 1691efc8-f - Received
2024-03-20 13:11:21,226 INFO     - product_feeds | product_feeds.one_feed_update_requested | 63ea48f7-3 - Received
2024-03-20 13:11:21,226 INFO     - product_feeds | product_feeds.one_feed_update_requested | aaed55db-3 - Received
2024-03-20 13:11:21,226 INFO     - product_feeds | product_feeds.one_feed_update_requested | 0475ce5d-0 - Received
2024-03-20 13:11:21,227 INFO     - product_feeds | product_feeds.one_feed_update_requested | 8563d516-8 - Received
2024-03-20 13:11:21,227 INFO     - product_feeds | product_feeds.one_feed_update_requested | a0c2358e-9 - Received
2024-03-20 13:11:21,227 INFO     - product_feeds | product_feeds.one_feed_update_requested | f679d642-f - Received
2024-03-20 13:11:21,228 ERROR    - product_feeds | product_feeds.one_feed_update_requested | 8563d516-8 - ValidationError: 1 validation error for update_feed
feed_id
  Input should be a valid integer [type=int_type, input_value={'item': {'id': 33, 'titl...e': None}, 'feed_id': 1}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.6/v/int_type
Traceback (most recent call last):
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/handler.py", line 367, in consume
    raise e
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/handler.py", line 331, in consume
    result = await cast(
             ^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/utils.py", line 95, in set_message_wrapper
    return await func(message)
           ^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/nats/broker.py", line 244, in process_wrapper
    r = await func(message)
        ^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/core/asynchronous.py", line 406, in decode_wrapper
    return await func(msg)
           ^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/use.py", line 146, in injected_wrapper
    r = await real_model.asolve(
        ^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/core/model.py", line 519, in asolve
    final_args, final_kwargs, call = cast_gen.send(kwargs)
                                     ^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/core/model.py", line 274, in _solve
    casted_model = self.model(**solved_kw)
                   ^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/pydantic/main.py", line 171, in __init__
    self.__pydantic_validator__.validate_python(data, self_instance=self)
pydantic_core._pydantic_core.ValidationError: 1 validation error for update_feed
feed_id
  Input should be a valid integer [type=int_type, input_value={'item': {'id': 33, 'titl...e': None}, 'feed_id': 1}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.6/v/int_type
2024-03-20 13:11:21,238 INFO     - product_feeds | product_feeds.one_feed_update_requested | 8563d516-8 - Processed
2024-03-20 13:11:21,239 ERROR    - product_feeds | product_feeds.one_feed_update_requested | d13c8f2b-d - ValidationError: 1 validation error for update_feed
feed_id
  Input should be a valid integer [type=int_type, input_value={'item': {'id': 28, 'titl...e': None}, 'feed_id': 1}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.6/v/int_type
Traceback (most recent call last):
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/handler.py", line 367, in consume
    raise e
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/handler.py", line 331, in consume
    result = await cast(
             ^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/utils.py", line 95, in set_message_wrapper
    return await func(message)
           ^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/nats/broker.py", line 244, in process_wrapper
    r = await func(message)
        ^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/core/asynchronous.py", line 406, in decode_wrapper
    return await func(msg)
           ^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/use.py", line 146, in injected_wrapper
    r = await real_model.asolve(
        ^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/core/model.py", line 519, in asolve
    final_args, final_kwargs, call = cast_gen.send(kwargs)
                                     ^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/core/model.py", line 274, in _solve
    casted_model = self.model(**solved_kw)
                   ^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/pydantic/main.py", line 171, in __init__
    self.__pydantic_validator__.validate_python(data, self_instance=self)
pydantic_core._pydantic_core.ValidationError: 1 validation error for update_feed
feed_id
  Input should be a valid integer [type=int_type, input_value={'item': {'id': 28, 'titl...e': None}, 'feed_id': 1}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.6/v/int_type
2024-03-20 13:11:21,240 INFO     - product_feeds | product_feeds.one_feed_update_requested | d13c8f2b-d - Processed
2024-03-20 13:11:21,240 ERROR    - product_feeds | product_feeds.one_feed_update_requested | aaed55db-3 - ValidationError: 1 validation error for update_feed
feed_id
  Input should be a valid integer [type=int_type, input_value={'item': {'id': 31, 'titl...e': None}, 'feed_id': 1}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.6/v/int_type
Traceback (most recent call last):
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/handler.py", line 367, in consume
    raise e
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/handler.py", line 331, in consume
    result = await cast(
             ^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/utils.py", line 95, in set_message_wrapper
    return await func(message)
           ^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/nats/broker.py", line 244, in process_wrapper
    r = await func(message)
        ^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/core/asynchronous.py", line 406, in decode_wrapper
    return await func(msg)
           ^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/use.py", line 146, in injected_wrapper
    r = await real_model.asolve(
        ^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/core/model.py", line 519, in asolve
    final_args, final_kwargs, call = cast_gen.send(kwargs)
                                     ^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/core/model.py", line 274, in _solve
    casted_model = self.model(**solved_kw)
                   ^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/pydantic/main.py", line 171, in __init__
    self.__pydantic_validator__.validate_python(data, self_instance=self)
pydantic_core._pydantic_core.ValidationError: 1 validation error for update_feed
feed_id
  Input should be a valid integer [type=int_type, input_value={'item': {'id': 31, 'titl...e': None}, 'feed_id': 1}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.6/v/int_type
2024-03-20 13:11:21,241 INFO     - product_feeds | product_feeds.one_feed_update_requested | aaed55db-3 - Processed
2024-03-20 13:11:21,241 ERROR    - product_feeds | product_feeds.one_feed_update_requested | a0c2358e-9 - ValidationError: 1 validation error for update_feed
feed_id
  Input should be a valid integer [type=int_type, input_value={'item': {'id': 34, 'titl...e': None}, 'feed_id': 1}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.6/v/int_type
Traceback (most recent call last):
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/handler.py", line 367, in consume
    raise e
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/handler.py", line 331, in consume
    result = await cast(
             ^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/utils.py", line 95, in set_message_wrapper
    return await func(message)
           ^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/nats/broker.py", line 244, in process_wrapper
    r = await func(message)
        ^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/core/asynchronous.py", line 406, in decode_wrapper
    return await func(msg)
           ^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/use.py", line 146, in injected_wrapper
    r = await real_model.asolve(
        ^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/core/model.py", line 519, in asolve
    final_args, final_kwargs, call = cast_gen.send(kwargs)
                                     ^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/core/model.py", line 274, in _solve
    casted_model = self.model(**solved_kw)
                   ^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/pydantic/main.py", line 171, in __init__
    self.__pydantic_validator__.validate_python(data, self_instance=self)
pydantic_core._pydantic_core.ValidationError: 1 validation error for update_feed
feed_id
  Input should be a valid integer [type=int_type, input_value={'item': {'id': 34, 'titl...e': None}, 'feed_id': 1}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.6/v/int_type
2024-03-20 13:11:21,242 INFO     - product_feeds | product_feeds.one_feed_update_requested | a0c2358e-9 - Processed
2024-03-20 13:11:21,242 ERROR    - product_feeds | product_feeds.one_feed_update_requested | f679d642-f - ValidationError: 1 validation error for update_feed
feed_id
  Input should be a valid integer [type=int_type, input_value={'item': {'id': 35, 'titl...e': None}, 'feed_id': 1}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.6/v/int_type
Traceback (most recent call last):
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/handler.py", line 367, in consume
    raise e
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/handler.py", line 331, in consume
    result = await cast(
             ^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/utils.py", line 95, in set_message_wrapper
    return await func(message)
           ^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/nats/broker.py", line 244, in process_wrapper
    r = await func(message)
        ^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/core/asynchronous.py", line 406, in decode_wrapper
    return await func(msg)
           ^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/use.py", line 146, in injected_wrapper
    r = await real_model.asolve(
        ^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/core/model.py", line 519, in asolve
    final_args, final_kwargs, call = cast_gen.send(kwargs)
                                     ^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/core/model.py", line 274, in _solve
    casted_model = self.model(**solved_kw)
                   ^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/pydantic/main.py", line 171, in __init__
    self.__pydantic_validator__.validate_python(data, self_instance=self)
pydantic_core._pydantic_core.ValidationError: 1 validation error for update_feed
feed_id
  Input should be a valid integer [type=int_type, input_value={'item': {'id': 35, 'titl...e': None}, 'feed_id': 1}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.6/v/int_type
2024-03-20 13:11:21,243 INFO     - product_feeds | product_feeds.one_feed_update_requested | f679d642-f - Processed
2024-03-20 13:11:21,243 ERROR    - product_feeds | product_feeds.one_feed_update_requested | 1691efc8-f - ValidationError: 1 validation error for update_feed
feed_id
  Input should be a valid integer [type=int_type, input_value={'item': {'id': 29, 'titl...e': None}, 'feed_id': 1}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.6/v/int_type
Traceback (most recent call last):
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/handler.py", line 367, in consume
    raise e
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/handler.py", line 331, in consume
    result = await cast(
             ^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/utils.py", line 95, in set_message_wrapper
    return await func(message)
           ^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/nats/broker.py", line 244, in process_wrapper
    r = await func(message)
        ^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/core/asynchronous.py", line 406, in decode_wrapper
    return await func(msg)
           ^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/use.py", line 146, in injected_wrapper
    r = await real_model.asolve(
        ^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/core/model.py", line 519, in asolve
    final_args, final_kwargs, call = cast_gen.send(kwargs)
                                     ^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/core/model.py", line 274, in _solve
    casted_model = self.model(**solved_kw)
                   ^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/pydantic/main.py", line 171, in __init__
    self.__pydantic_validator__.validate_python(data, self_instance=self)
pydantic_core._pydantic_core.ValidationError: 1 validation error for update_feed
feed_id
  Input should be a valid integer [type=int_type, input_value={'item': {'id': 29, 'titl...e': None}, 'feed_id': 1}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.6/v/int_type
2024-03-20 13:11:21,244 INFO     - product_feeds | product_feeds.one_feed_update_requested | 1691efc8-f - Processed
2024-03-20 13:11:21,244 ERROR    - product_feeds | product_feeds.one_feed_update_requested | 0475ce5d-0 - ValidationError: 1 validation error for update_feed
feed_id
  Input should be a valid integer [type=int_type, input_value={'item': {'id': 32, 'titl...e': None}, 'feed_id': 1}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.6/v/int_type
Traceback (most recent call last):
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/handler.py", line 367, in consume
    raise e
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/handler.py", line 331, in consume
    result = await cast(
             ^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/utils.py", line 95, in set_message_wrapper
    return await func(message)
           ^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/nats/broker.py", line 244, in process_wrapper
    r = await func(message)
        ^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/core/asynchronous.py", line 406, in decode_wrapper
    return await func(msg)
           ^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/use.py", line 146, in injected_wrapper
    r = await real_model.asolve(
        ^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/core/model.py", line 519, in asolve
    final_args, final_kwargs, call = cast_gen.send(kwargs)
                                     ^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/core/model.py", line 274, in _solve
    casted_model = self.model(**solved_kw)
                   ^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/pydantic/main.py", line 171, in __init__
    self.__pydantic_validator__.validate_python(data, self_instance=self)
pydantic_core._pydantic_core.ValidationError: 1 validation error for update_feed
feed_id
  Input should be a valid integer [type=int_type, input_value={'item': {'id': 32, 'titl...e': None}, 'feed_id': 1}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.6/v/int_type
2024-03-20 13:11:21,245 INFO     - product_feeds | product_feeds.one_feed_update_requested | 0475ce5d-0 - Processed
2024-03-20 13:11:21,245 ERROR    - product_feeds | product_feeds.one_feed_update_requested | 1521f974-7 - ValidationError: 1 validation error for update_feed
feed_id
  Input should be a valid integer [type=int_type, input_value={'item': {'id': 26, 'titl...e': None}, 'feed_id': 1}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.6/v/int_type
Traceback (most recent call last):
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/handler.py", line 367, in consume
    raise e
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/handler.py", line 331, in consume
    result = await cast(
             ^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/utils.py", line 95, in set_message_wrapper
    return await func(message)
           ^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/nats/broker.py", line 244, in process_wrapper
    r = await func(message)
        ^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/core/asynchronous.py", line 406, in decode_wrapper
    return await func(msg)
           ^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/use.py", line 146, in injected_wrapper
    r = await real_model.asolve(
        ^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/core/model.py", line 519, in asolve
    final_args, final_kwargs, call = cast_gen.send(kwargs)
                                     ^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/core/model.py", line 274, in _solve
    casted_model = self.model(**solved_kw)
                   ^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/pydantic/main.py", line 171, in __init__
    self.__pydantic_validator__.validate_python(data, self_instance=self)
pydantic_core._pydantic_core.ValidationError: 1 validation error for update_feed
feed_id
  Input should be a valid integer [type=int_type, input_value={'item': {'id': 26, 'titl...e': None}, 'feed_id': 1}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.6/v/int_type
2024-03-20 13:11:21,246 INFO     - product_feeds | product_feeds.one_feed_update_requested | 1521f974-7 - Processed
2024-03-20 13:11:21,246 ERROR    - product_feeds | product_feeds.one_feed_update_requested | 63ea48f7-3 - ValidationError: 1 validation error for update_feed
feed_id
  Input should be a valid integer [type=int_type, input_value={'item': {'id': 30, 'titl...e': None}, 'feed_id': 1}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.6/v/int_type
Traceback (most recent call last):
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/handler.py", line 367, in consume
    raise e
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/handler.py", line 331, in consume
    result = await cast(
             ^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/utils.py", line 95, in set_message_wrapper
    return await func(message)
           ^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/nats/broker.py", line 244, in process_wrapper
    r = await func(message)
        ^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/core/asynchronous.py", line 406, in decode_wrapper
    return await func(msg)
           ^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/use.py", line 146, in injected_wrapper
    r = await real_model.asolve(
        ^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/core/model.py", line 519, in asolve
    final_args, final_kwargs, call = cast_gen.send(kwargs)
                                     ^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/core/model.py", line 274, in _solve
    casted_model = self.model(**solved_kw)
                   ^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/pydantic/main.py", line 171, in __init__
    self.__pydantic_validator__.validate_python(data, self_instance=self)
pydantic_core._pydantic_core.ValidationError: 1 validation error for update_feed
feed_id
  Input should be a valid integer [type=int_type, input_value={'item': {'id': 30, 'titl...e': None}, 'feed_id': 1}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.6/v/int_type
2024-03-20 13:11:21,247 INFO     - product_feeds | product_feeds.one_feed_update_requested | 63ea48f7-3 - Processed
2024-03-20 13:11:21,247 ERROR    - product_feeds | product_feeds.one_feed_update_requested | 7fbcc7cf-c - ValidationError: 1 validation error for update_feed
feed_id
  Input should be a valid integer [type=int_type, input_value={'item': {'id': 27, 'titl...e': None}, 'feed_id': 1}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.6/v/int_type
Traceback (most recent call last):
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/handler.py", line 367, in consume
    raise e
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/handler.py", line 331, in consume
    result = await cast(
             ^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/utils.py", line 95, in set_message_wrapper
    return await func(message)
           ^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/nats/broker.py", line 244, in process_wrapper
    r = await func(message)
        ^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/core/asynchronous.py", line 406, in decode_wrapper
    return await func(msg)
           ^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/use.py", line 146, in injected_wrapper
    r = await real_model.asolve(
        ^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/core/model.py", line 519, in asolve
    final_args, final_kwargs, call = cast_gen.send(kwargs)
                                     ^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/core/model.py", line 274, in _solve
    casted_model = self.model(**solved_kw)
                   ^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/pydantic/main.py", line 171, in __init__
    self.__pydantic_validator__.validate_python(data, self_instance=self)
pydantic_core._pydantic_core.ValidationError: 1 validation error for update_feed
feed_id
  Input should be a valid integer [type=int_type, input_value={'item': {'id': 27, 'titl...e': None}, 'feed_id': 1}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.6/v/int_type
2024-03-20 13:11:21,247 INFO     - product_feeds | product_feeds.one_feed_update_requested | 7fbcc7cf-c - Processed
2024-03-20 13:11:21,251 INFO     - product_feeds | product_feeds.one_feed_update_requested | 09269759-f - Received
2024-03-20 13:11:21,251 INFO     - product_feeds | product_feeds.one_feed_update_requested | d1ae745f-4 - Received
2024-03-20 13:11:21,251 INFO     - product_feeds | product_feeds.one_feed_update_requested | 47d19cfc-c - Received
2024-03-20 13:11:21,251 INFO     - product_feeds | product_feeds.one_feed_update_requested | ef848520-d - Received
2024-03-20 13:11:21,251 INFO     - product_feeds | product_feeds.one_feed_update_requested | 5c2f0b37-2 - Received
2024-03-20 13:11:21,251 INFO     - product_feeds | product_feeds.one_feed_update_requested | 0987fbc0-d - Received
2024-03-20 13:11:21,251 INFO     - product_feeds | product_feeds.one_feed_update_requested | f7e42b52-a - Received
2024-03-20 13:11:21,251 INFO     - product_feeds | product_feeds.one_feed_update_requested | cb913980-c - Received
2024-03-20 13:11:21,251 INFO     - product_feeds | product_feeds.one_feed_update_requested | 5546ea26-1 - Received
2024-03-20 13:11:21,252 INFO     - product_feeds | product_feeds.one_feed_update_requested | 67ec4934-2 - Received
2024-03-20 13:11:21,258 ERROR    - product_feeds | product_feeds.one_feed_update_requested | 0987fbc0-d - ValidationError: 1 validation error for update_feed
feed_id
  Input should be a valid integer [type=int_type, input_value={'item': {'id': 41, 'titl...e': None}, 'feed_id': 1}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.6/v/int_type
Traceback (most recent call last):
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/handler.py", line 367, in consume
    raise e
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/handler.py", line 331, in consume
    result = await cast(
             ^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/utils.py", line 95, in set_message_wrapper
    return await func(message)
           ^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/nats/broker.py", line 244, in process_wrapper
    r = await func(message)
        ^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/core/asynchronous.py", line 406, in decode_wrapper
    return await func(msg)
           ^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/use.py", line 146, in injected_wrapper
    r = await real_model.asolve(
        ^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/core/model.py", line 519, in asolve
    final_args, final_kwargs, call = cast_gen.send(kwargs)
                                     ^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/core/model.py", line 274, in _solve
    casted_model = self.model(**solved_kw)
                   ^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/pydantic/main.py", line 171, in __init__
    self.__pydantic_validator__.validate_python(data, self_instance=self)
pydantic_core._pydantic_core.ValidationError: 1 validation error for update_feed
feed_id
  Input should be a valid integer [type=int_type, input_value={'item': {'id': 41, 'titl...e': None}, 'feed_id': 1}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.6/v/int_type
2024-03-20 13:11:21,259 INFO     - product_feeds | product_feeds.one_feed_update_requested | 0987fbc0-d - Processed
2024-03-20 13:11:21,259 ERROR    - product_feeds | product_feeds.one_feed_update_requested | 5c2f0b37-2 - ValidationError: 1 validation error for update_feed
feed_id
  Input should be a valid integer [type=int_type, input_value={'item': {'id': 40, 'titl...e': None}, 'feed_id': 1}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.6/v/int_type
Traceback (most recent call last):
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/handler.py", line 367, in consume
    raise e
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/handler.py", line 331, in consume
    result = await cast(
             ^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/utils.py", line 95, in set_message_wrapper
    return await func(message)
           ^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/nats/broker.py", line 244, in process_wrapper
    r = await func(message)
        ^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/core/asynchronous.py", line 406, in decode_wrapper
    return await func(msg)
           ^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/use.py", line 146, in injected_wrapper
    r = await real_model.asolve(
        ^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/core/model.py", line 519, in asolve
    final_args, final_kwargs, call = cast_gen.send(kwargs)
                                     ^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/core/model.py", line 274, in _solve
    casted_model = self.model(**solved_kw)
                   ^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/pydantic/main.py", line 171, in __init__
    self.__pydantic_validator__.validate_python(data, self_instance=self)
pydantic_core._pydantic_core.ValidationError: 1 validation error for update_feed
feed_id
  Input should be a valid integer [type=int_type, input_value={'item': {'id': 40, 'titl...e': None}, 'feed_id': 1}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.6/v/int_type
2024-03-20 13:11:21,260 INFO     - product_feeds | product_feeds.one_feed_update_requested | 5c2f0b37-2 - Processed
2024-03-20 13:11:21,260 ERROR    - product_feeds | product_feeds.one_feed_update_requested | 47d19cfc-c - ValidationError: 1 validation error for update_feed
feed_id
  Input should be a valid integer [type=int_type, input_value={'item': {'id': 38, 'titl...e': None}, 'feed_id': 1}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.6/v/int_type
Traceback (most recent call last):
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/handler.py", line 367, in consume
    raise e
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/handler.py", line 331, in consume
    result = await cast(
             ^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/utils.py", line 95, in set_message_wrapper
    return await func(message)
           ^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/nats/broker.py", line 244, in process_wrapper
    r = await func(message)
        ^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/core/asynchronous.py", line 406, in decode_wrapper
    return await func(msg)
           ^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/use.py", line 146, in injected_wrapper
    r = await real_model.asolve(
        ^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/core/model.py", line 519, in asolve
    final_args, final_kwargs, call = cast_gen.send(kwargs)
                                     ^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/core/model.py", line 274, in _solve
    casted_model = self.model(**solved_kw)
                   ^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/pydantic/main.py", line 171, in __init__
    self.__pydantic_validator__.validate_python(data, self_instance=self)
pydantic_core._pydantic_core.ValidationError: 1 validation error for update_feed
feed_id
  Input should be a valid integer [type=int_type, input_value={'item': {'id': 38, 'titl...e': None}, 'feed_id': 1}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.6/v/int_type
2024-03-20 13:11:21,261 INFO     - product_feeds | product_feeds.one_feed_update_requested | 47d19cfc-c - Processed
2024-03-20 13:11:21,261 ERROR    - product_feeds | product_feeds.one_feed_update_requested | 67ec4934-2 - ValidationError: 1 validation error for update_feed
feed_id
  Input should be a valid integer [type=int_type, input_value={'item': {'id': 45, 'titl...e': None}, 'feed_id': 1}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.6/v/int_type
Traceback (most recent call last):
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/handler.py", line 367, in consume
    raise e
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/handler.py", line 331, in consume
    result = await cast(
             ^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/utils.py", line 95, in set_message_wrapper
    return await func(message)
           ^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/nats/broker.py", line 244, in process_wrapper
    r = await func(message)
        ^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/core/asynchronous.py", line 406, in decode_wrapper
    return await func(msg)
           ^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/use.py", line 146, in injected_wrapper
    r = await real_model.asolve(
        ^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/core/model.py", line 519, in asolve
    final_args, final_kwargs, call = cast_gen.send(kwargs)
                                     ^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/core/model.py", line 274, in _solve
    casted_model = self.model(**solved_kw)
                   ^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/pydantic/main.py", line 171, in __init__
    self.__pydantic_validator__.validate_python(data, self_instance=self)
pydantic_core._pydantic_core.ValidationError: 1 validation error for update_feed
feed_id
  Input should be a valid integer [type=int_type, input_value={'item': {'id': 45, 'titl...e': None}, 'feed_id': 1}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.6/v/int_type
2024-03-20 13:11:21,262 INFO     - product_feeds | product_feeds.one_feed_update_requested | 67ec4934-2 - Processed
2024-03-20 13:11:21,262 ERROR    - product_feeds | product_feeds.one_feed_update_requested | d1ae745f-4 - ValidationError: 1 validation error for update_feed
feed_id
  Input should be a valid integer [type=int_type, input_value={'item': {'id': 37, 'titl...e': None}, 'feed_id': 1}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.6/v/int_type
Traceback (most recent call last):
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/handler.py", line 367, in consume
    raise e
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/handler.py", line 331, in consume
    result = await cast(
             ^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/utils.py", line 95, in set_message_wrapper
    return await func(message)
           ^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/nats/broker.py", line 244, in process_wrapper
    r = await func(message)
        ^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/core/asynchronous.py", line 406, in decode_wrapper
    return await func(msg)
           ^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/use.py", line 146, in injected_wrapper
    r = await real_model.asolve(
        ^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/core/model.py", line 519, in asolve
    final_args, final_kwargs, call = cast_gen.send(kwargs)
                                     ^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/core/model.py", line 274, in _solve
    casted_model = self.model(**solved_kw)
                   ^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/pydantic/main.py", line 171, in __init__
    self.__pydantic_validator__.validate_python(data, self_instance=self)
pydantic_core._pydantic_core.ValidationError: 1 validation error for update_feed
feed_id
  Input should be a valid integer [type=int_type, input_value={'item': {'id': 37, 'titl...e': None}, 'feed_id': 1}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.6/v/int_type
2024-03-20 13:11:21,263 INFO     - product_feeds | product_feeds.one_feed_update_requested | d1ae745f-4 - Processed
2024-03-20 13:11:21,263 ERROR    - product_feeds | product_feeds.one_feed_update_requested | 5546ea26-1 - ValidationError: 1 validation error for update_feed
feed_id
  Input should be a valid integer [type=int_type, input_value={'item': {'id': 44, 'titl...e': None}, 'feed_id': 1}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.6/v/int_type
Traceback (most recent call last):
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/handler.py", line 367, in consume
    raise e
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/handler.py", line 331, in consume
    result = await cast(
             ^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/utils.py", line 95, in set_message_wrapper
    return await func(message)
           ^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/nats/broker.py", line 244, in process_wrapper
    r = await func(message)
        ^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/core/asynchronous.py", line 406, in decode_wrapper
    return await func(msg)
           ^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/use.py", line 146, in injected_wrapper
    r = await real_model.asolve(
        ^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/core/model.py", line 519, in asolve
    final_args, final_kwargs, call = cast_gen.send(kwargs)
                                     ^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/core/model.py", line 274, in _solve
    casted_model = self.model(**solved_kw)
                   ^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/pydantic/main.py", line 171, in __init__
    self.__pydantic_validator__.validate_python(data, self_instance=self)
pydantic_core._pydantic_core.ValidationError: 1 validation error for update_feed
feed_id
  Input should be a valid integer [type=int_type, input_value={'item': {'id': 44, 'titl...e': None}, 'feed_id': 1}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.6/v/int_type
2024-03-20 13:11:21,264 INFO     - product_feeds | product_feeds.one_feed_update_requested | 5546ea26-1 - Processed
2024-03-20 13:11:21,264 ERROR    - product_feeds | product_feeds.one_feed_update_requested | ef848520-d - ValidationError: 1 validation error for update_feed
feed_id
  Input should be a valid integer [type=int_type, input_value={'item': {'id': 39, 'titl...e': None}, 'feed_id': 1}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.6/v/int_type
Traceback (most recent call last):
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/handler.py", line 367, in consume
    raise e
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/handler.py", line 331, in consume
    result = await cast(
             ^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/utils.py", line 95, in set_message_wrapper
    return await func(message)
           ^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/nats/broker.py", line 244, in process_wrapper
    r = await func(message)
        ^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/core/asynchronous.py", line 406, in decode_wrapper
    return await func(msg)
           ^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/use.py", line 146, in injected_wrapper
    r = await real_model.asolve(
        ^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/core/model.py", line 519, in asolve
    final_args, final_kwargs, call = cast_gen.send(kwargs)
                                     ^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/core/model.py", line 274, in _solve
    casted_model = self.model(**solved_kw)
                   ^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/pydantic/main.py", line 171, in __init__
    self.__pydantic_validator__.validate_python(data, self_instance=self)
pydantic_core._pydantic_core.ValidationError: 1 validation error for update_feed
feed_id
  Input should be a valid integer [type=int_type, input_value={'item': {'id': 39, 'titl...e': None}, 'feed_id': 1}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.6/v/int_type
2024-03-20 13:11:21,265 INFO     - product_feeds | product_feeds.one_feed_update_requested | ef848520-d - Processed
2024-03-20 13:11:21,265 ERROR    - product_feeds | product_feeds.one_feed_update_requested | 09269759-f - ValidationError: 1 validation error for update_feed
feed_id
  Input should be a valid integer [type=int_type, input_value={'item': {'id': 36, 'titl...e': None}, 'feed_id': 1}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.6/v/int_type
Traceback (most recent call last):
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/handler.py", line 367, in consume
    raise e
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/handler.py", line 331, in consume
    result = await cast(
             ^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/utils.py", line 95, in set_message_wrapper
    return await func(message)
           ^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/nats/broker.py", line 244, in process_wrapper
    r = await func(message)
        ^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/core/asynchronous.py", line 406, in decode_wrapper
    return await func(msg)
           ^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/use.py", line 146, in injected_wrapper
    r = await real_model.asolve(
        ^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/core/model.py", line 519, in asolve
    final_args, final_kwargs, call = cast_gen.send(kwargs)
                                     ^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/core/model.py", line 274, in _solve
    casted_model = self.model(**solved_kw)
                   ^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/pydantic/main.py", line 171, in __init__
    self.__pydantic_validator__.validate_python(data, self_instance=self)
pydantic_core._pydantic_core.ValidationError: 1 validation error for update_feed
feed_id
  Input should be a valid integer [type=int_type, input_value={'item': {'id': 36, 'titl...e': None}, 'feed_id': 1}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.6/v/int_type
2024-03-20 13:11:21,266 INFO     - product_feeds | product_feeds.one_feed_update_requested | 09269759-f - Processed
2024-03-20 13:11:21,266 ERROR    - product_feeds | product_feeds.one_feed_update_requested | cb913980-c - ValidationError: 1 validation error for update_feed
feed_id
  Input should be a valid integer [type=int_type, input_value={'item': {'id': 43, 'titl...e': None}, 'feed_id': 1}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.6/v/int_type
Traceback (most recent call last):
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/handler.py", line 367, in consume
    raise e
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/handler.py", line 331, in consume
    result = await cast(
             ^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/utils.py", line 95, in set_message_wrapper
    return await func(message)
           ^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/nats/broker.py", line 244, in process_wrapper
    r = await func(message)
        ^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/core/asynchronous.py", line 406, in decode_wrapper
    return await func(msg)
           ^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/use.py", line 146, in injected_wrapper
    r = await real_model.asolve(
        ^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/core/model.py", line 519, in asolve
    final_args, final_kwargs, call = cast_gen.send(kwargs)
                                     ^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/core/model.py", line 274, in _solve
    casted_model = self.model(**solved_kw)
                   ^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/pydantic/main.py", line 171, in __init__
    self.__pydantic_validator__.validate_python(data, self_instance=self)
pydantic_core._pydantic_core.ValidationError: 1 validation error for update_feed
feed_id
  Input should be a valid integer [type=int_type, input_value={'item': {'id': 43, 'titl...e': None}, 'feed_id': 1}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.6/v/int_type
2024-03-20 13:11:21,267 INFO     - product_feeds | product_feeds.one_feed_update_requested | cb913980-c - Processed
2024-03-20 13:11:21,267 ERROR    - product_feeds | product_feeds.one_feed_update_requested | f7e42b52-a - ValidationError: 1 validation error for update_feed
feed_id
  Input should be a valid integer [type=int_type, input_value={'item': {'id': 42, 'titl...e': None}, 'feed_id': 1}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.6/v/int_type
Traceback (most recent call last):
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/handler.py", line 367, in consume
    raise e
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/handler.py", line 331, in consume
    result = await cast(
             ^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/utils.py", line 95, in set_message_wrapper
    return await func(message)
           ^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/nats/broker.py", line 244, in process_wrapper
    r = await func(message)
        ^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/core/asynchronous.py", line 406, in decode_wrapper
    return await func(msg)
           ^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/use.py", line 146, in injected_wrapper
    r = await real_model.asolve(
        ^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/core/model.py", line 519, in asolve
    final_args, final_kwargs, call = cast_gen.send(kwargs)
                                     ^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/core/model.py", line 274, in _solve
    casted_model = self.model(**solved_kw)
                   ^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/pydantic/main.py", line 171, in __init__
    self.__pydantic_validator__.validate_python(data, self_instance=self)
pydantic_core._pydantic_core.ValidationError: 1 validation error for update_feed
feed_id
  Input should be a valid integer [type=int_type, input_value={'item': {'id': 42, 'titl...e': None}, 'feed_id': 1}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.6/v/int_type
2024-03-20 13:11:21,268 INFO     - product_feeds | product_feeds.one_feed_update_requested | f7e42b52-a - Processed
2024-03-20 13:11:21,270 INFO     - product_feeds | product_feeds.one_feed_update_requested | e21ac3c4-a - Received
2024-03-20 13:11:21,270 INFO     - product_feeds | product_feeds.one_feed_update_requested | 24badc47-c - Received
2024-03-20 13:11:21,270 INFO     - product_feeds | product_feeds.one_feed_update_requested | e3d54fa0-0 - Received
2024-03-20 13:11:21,270 INFO     - product_feeds | product_feeds.one_feed_update_requested | f0f3cef4-6 - Received
2024-03-20 13:11:21,271 INFO     - product_feeds | product_feeds.one_feed_update_requested | fb9a1874-1 - Received
2024-03-20 13:11:21,271 INFO     - product_feeds | product_feeds.one_feed_update_requested | 1d6763d0-1 - Received
2024-03-20 13:11:21,271 INFO     - product_feeds | product_feeds.one_feed_update_requested | 2ea556f4-5 - Received
2024-03-20 13:11:21,271 INFO     - product_feeds | product_feeds.one_feed_update_requested | 1981c39e-2 - Received
2024-03-20 13:11:21,271 INFO     - product_feeds | product_feeds.one_feed_update_requested | 2a82795b-7 - Received
2024-03-20 13:11:21,271 INFO     - product_feeds | product_feeds.one_feed_update_requested | d456cc15-d - Received
2024-03-20 13:11:21,278 ERROR    - product_feeds | product_feeds.one_feed_update_requested | 1d6763d0-1 - ValidationError: 1 validation error for update_feed
feed_id
  Input should be a valid integer [type=int_type, input_value={'item': {'id': 51, 'titl...e': None}, 'feed_id': 1}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.6/v/int_type
Traceback (most recent call last):
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/handler.py", line 367, in consume
    raise e
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/handler.py", line 331, in consume
    result = await cast(
             ^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/utils.py", line 95, in set_message_wrapper
    return await func(message)
           ^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/nats/broker.py", line 244, in process_wrapper
    r = await func(message)
        ^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/core/asynchronous.py", line 406, in decode_wrapper
    return await func(msg)
           ^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/use.py", line 146, in injected_wrapper
    r = await real_model.asolve(
        ^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/core/model.py", line 519, in asolve
    final_args, final_kwargs, call = cast_gen.send(kwargs)
                                     ^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/core/model.py", line 274, in _solve
    casted_model = self.model(**solved_kw)
                   ^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/pydantic/main.py", line 171, in __init__
    self.__pydantic_validator__.validate_python(data, self_instance=self)
pydantic_core._pydantic_core.ValidationError: 1 validation error for update_feed
feed_id
  Input should be a valid integer [type=int_type, input_value={'item': {'id': 51, 'titl...e': None}, 'feed_id': 1}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.6/v/int_type
2024-03-20 13:11:21,279 INFO     - product_feeds | product_feeds.one_feed_update_requested | 1d6763d0-1 - Processed
2024-03-20 13:11:21,280 ERROR    - product_feeds | product_feeds.one_feed_update_requested | 2ea556f4-5 - ValidationError: 1 validation error for update_feed
feed_id
  Input should be a valid integer [type=int_type, input_value={'item': {'id': 52, 'titl...e': None}, 'feed_id': 1}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.6/v/int_type
Traceback (most recent call last):
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/handler.py", line 367, in consume
    raise e
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/handler.py", line 331, in consume
    result = await cast(
             ^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/utils.py", line 95, in set_message_wrapper
    return await func(message)
           ^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/nats/broker.py", line 244, in process_wrapper
    r = await func(message)
        ^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/core/asynchronous.py", line 406, in decode_wrapper
    return await func(msg)
           ^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/use.py", line 146, in injected_wrapper
    r = await real_model.asolve(
        ^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/core/model.py", line 519, in asolve
    final_args, final_kwargs, call = cast_gen.send(kwargs)
                                     ^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/core/model.py", line 274, in _solve
    casted_model = self.model(**solved_kw)
                   ^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/pydantic/main.py", line 171, in __init__
    self.__pydantic_validator__.validate_python(data, self_instance=self)
pydantic_core._pydantic_core.ValidationError: 1 validation error for update_feed
feed_id
  Input should be a valid integer [type=int_type, input_value={'item': {'id': 52, 'titl...e': None}, 'feed_id': 1}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.6/v/int_type
2024-03-20 13:11:21,280 INFO     - product_feeds | product_feeds.one_feed_update_requested | 2ea556f4-5 - Processed
2024-03-20 13:11:21,280 ERROR    - product_feeds | product_feeds.one_feed_update_requested | fb9a1874-1 - ValidationError: 1 validation error for update_feed
feed_id
  Input should be a valid integer [type=int_type, input_value={'item': {'id': 50, 'titl...e': None}, 'feed_id': 1}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.6/v/int_type
Traceback (most recent call last):
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/handler.py", line 367, in consume
    raise e
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/handler.py", line 331, in consume
    result = await cast(
             ^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/utils.py", line 95, in set_message_wrapper
    return await func(message)
           ^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/nats/broker.py", line 244, in process_wrapper
    r = await func(message)
        ^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/core/asynchronous.py", line 406, in decode_wrapper
    return await func(msg)
           ^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/use.py", line 146, in injected_wrapper
    r = await real_model.asolve(
        ^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/core/model.py", line 519, in asolve
    final_args, final_kwargs, call = cast_gen.send(kwargs)
                                     ^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/core/model.py", line 274, in _solve
    casted_model = self.model(**solved_kw)
                   ^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/pydantic/main.py", line 171, in __init__
    self.__pydantic_validator__.validate_python(data, self_instance=self)
pydantic_core._pydantic_core.ValidationError: 1 validation error for update_feed
feed_id
  Input should be a valid integer [type=int_type, input_value={'item': {'id': 50, 'titl...e': None}, 'feed_id': 1}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.6/v/int_type
2024-03-20 13:11:21,281 INFO     - product_feeds | product_feeds.one_feed_update_requested | fb9a1874-1 - Processed
2024-03-20 13:11:21,281 ERROR    - product_feeds | product_feeds.one_feed_update_requested | e3d54fa0-0 - ValidationError: 1 validation error for update_feed
feed_id
  Input should be a valid integer [type=int_type, input_value={'item': {'id': 48, 'titl...e': None}, 'feed_id': 1}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.6/v/int_type
Traceback (most recent call last):
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/handler.py", line 367, in consume
    raise e
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/handler.py", line 331, in consume
    result = await cast(
             ^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/utils.py", line 95, in set_message_wrapper
    return await func(message)
           ^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/nats/broker.py", line 244, in process_wrapper
    r = await func(message)
        ^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/core/asynchronous.py", line 406, in decode_wrapper
    return await func(msg)
           ^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/use.py", line 146, in injected_wrapper
    r = await real_model.asolve(
        ^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/core/model.py", line 519, in asolve
    final_args, final_kwargs, call = cast_gen.send(kwargs)
                                     ^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/core/model.py", line 274, in _solve
    casted_model = self.model(**solved_kw)
                   ^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/pydantic/main.py", line 171, in __init__
    self.__pydantic_validator__.validate_python(data, self_instance=self)
pydantic_core._pydantic_core.ValidationError: 1 validation error for update_feed
feed_id
  Input should be a valid integer [type=int_type, input_value={'item': {'id': 48, 'titl...e': None}, 'feed_id': 1}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.6/v/int_type
2024-03-20 13:11:21,282 INFO     - product_feeds | product_feeds.one_feed_update_requested | e3d54fa0-0 - Processed
2024-03-20 13:11:21,282 ERROR    - product_feeds | product_feeds.one_feed_update_requested | e21ac3c4-a - ValidationError: 1 validation error for update_feed
feed_id
  Input should be a valid integer [type=int_type, input_value={'item': {'id': 46, 'titl...e': None}, 'feed_id': 1}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.6/v/int_type
Traceback (most recent call last):
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/handler.py", line 367, in consume
    raise e
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/handler.py", line 331, in consume
    result = await cast(
             ^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/utils.py", line 95, in set_message_wrapper
    return await func(message)
           ^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/nats/broker.py", line 244, in process_wrapper
    r = await func(message)
        ^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/core/asynchronous.py", line 406, in decode_wrapper
    return await func(msg)
           ^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/use.py", line 146, in injected_wrapper
    r = await real_model.asolve(
        ^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/core/model.py", line 519, in asolve
    final_args, final_kwargs, call = cast_gen.send(kwargs)
                                     ^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/core/model.py", line 274, in _solve
    casted_model = self.model(**solved_kw)
                   ^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/pydantic/main.py", line 171, in __init__
    self.__pydantic_validator__.validate_python(data, self_instance=self)
pydantic_core._pydantic_core.ValidationError: 1 validation error for update_feed
feed_id
  Input should be a valid integer [type=int_type, input_value={'item': {'id': 46, 'titl...e': None}, 'feed_id': 1}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.6/v/int_type
2024-03-20 13:11:21,283 INFO     - product_feeds | product_feeds.one_feed_update_requested | e21ac3c4-a - Processed
2024-03-20 13:11:21,283 ERROR    - product_feeds | product_feeds.one_feed_update_requested | d456cc15-d - ValidationError: 1 validation error for update_feed
feed_id
  Input should be a valid integer [type=int_type, input_value={'item': {'id': 55, 'titl...e': None}, 'feed_id': 1}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.6/v/int_type
Traceback (most recent call last):
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/handler.py", line 367, in consume
    raise e
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/handler.py", line 331, in consume
    result = await cast(
             ^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/utils.py", line 95, in set_message_wrapper
    return await func(message)
           ^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/nats/broker.py", line 244, in process_wrapper
    r = await func(message)
        ^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/core/asynchronous.py", line 406, in decode_wrapper
    return await func(msg)
           ^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/use.py", line 146, in injected_wrapper
    r = await real_model.asolve(
        ^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/core/model.py", line 519, in asolve
    final_args, final_kwargs, call = cast_gen.send(kwargs)
                                     ^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/core/model.py", line 274, in _solve
    casted_model = self.model(**solved_kw)
                   ^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/pydantic/main.py", line 171, in __init__
    self.__pydantic_validator__.validate_python(data, self_instance=self)
pydantic_core._pydantic_core.ValidationError: 1 validation error for update_feed
feed_id
  Input should be a valid integer [type=int_type, input_value={'item': {'id': 55, 'titl...e': None}, 'feed_id': 1}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.6/v/int_type
2024-03-20 13:11:21,284 INFO     - product_feeds | product_feeds.one_feed_update_requested | d456cc15-d - Processed
2024-03-20 13:11:21,284 ERROR    - product_feeds | product_feeds.one_feed_update_requested | 1981c39e-2 - ValidationError: 1 validation error for update_feed
feed_id
  Input should be a valid integer [type=int_type, input_value={'item': {'id': 53, 'titl...e': None}, 'feed_id': 1}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.6/v/int_type
Traceback (most recent call last):
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/handler.py", line 367, in consume
    raise e
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/handler.py", line 331, in consume
    result = await cast(
             ^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/utils.py", line 95, in set_message_wrapper
    return await func(message)
           ^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/nats/broker.py", line 244, in process_wrapper
    r = await func(message)
        ^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/core/asynchronous.py", line 406, in decode_wrapper
    return await func(msg)
           ^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/use.py", line 146, in injected_wrapper
    r = await real_model.asolve(
        ^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/core/model.py", line 519, in asolve
    final_args, final_kwargs, call = cast_gen.send(kwargs)
                                     ^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/core/model.py", line 274, in _solve
    casted_model = self.model(**solved_kw)
                   ^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/pydantic/main.py", line 171, in __init__
    self.__pydantic_validator__.validate_python(data, self_instance=self)
pydantic_core._pydantic_core.ValidationError: 1 validation error for update_feed
feed_id
  Input should be a valid integer [type=int_type, input_value={'item': {'id': 53, 'titl...e': None}, 'feed_id': 1}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.6/v/int_type
2024-03-20 13:11:21,285 INFO     - product_feeds | product_feeds.one_feed_update_requested | 1981c39e-2 - Processed
2024-03-20 13:11:21,286 ERROR    - product_feeds | product_feeds.one_feed_update_requested | f0f3cef4-6 - ValidationError: 1 validation error for update_feed
feed_id
  Input should be a valid integer [type=int_type, input_value={'item': {'id': 49, 'titl...e': None}, 'feed_id': 1}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.6/v/int_type
Traceback (most recent call last):
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/handler.py", line 367, in consume
    raise e
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/handler.py", line 331, in consume
    result = await cast(
             ^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/utils.py", line 95, in set_message_wrapper
    return await func(message)
           ^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/nats/broker.py", line 244, in process_wrapper
    r = await func(message)
        ^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/core/asynchronous.py", line 406, in decode_wrapper
    return await func(msg)
           ^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/use.py", line 146, in injected_wrapper
    r = await real_model.asolve(
        ^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/core/model.py", line 519, in asolve
    final_args, final_kwargs, call = cast_gen.send(kwargs)
                                     ^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/core/model.py", line 274, in _solve
    casted_model = self.model(**solved_kw)
                   ^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/pydantic/main.py", line 171, in __init__
    self.__pydantic_validator__.validate_python(data, self_instance=self)
pydantic_core._pydantic_core.ValidationError: 1 validation error for update_feed
feed_id
  Input should be a valid integer [type=int_type, input_value={'item': {'id': 49, 'titl...e': None}, 'feed_id': 1}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.6/v/int_type
2024-03-20 13:11:21,287 INFO     - product_feeds | product_feeds.one_feed_update_requested | f0f3cef4-6 - Processed
2024-03-20 13:11:21,287 ERROR    - product_feeds | product_feeds.one_feed_update_requested | 24badc47-c - ValidationError: 1 validation error for update_feed
feed_id
  Input should be a valid integer [type=int_type, input_value={'item': {'id': 47, 'titl...e': None}, 'feed_id': 1}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.6/v/int_type
Traceback (most recent call last):
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/handler.py", line 367, in consume
    raise e
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/handler.py", line 331, in consume
    result = await cast(
             ^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/utils.py", line 95, in set_message_wrapper
    return await func(message)
           ^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/nats/broker.py", line 244, in process_wrapper
    r = await func(message)
        ^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/core/asynchronous.py", line 406, in decode_wrapper
    return await func(msg)
           ^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/use.py", line 146, in injected_wrapper
    r = await real_model.asolve(
        ^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/core/model.py", line 519, in asolve
    final_args, final_kwargs, call = cast_gen.send(kwargs)
                                     ^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/core/model.py", line 274, in _solve
    casted_model = self.model(**solved_kw)
                   ^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/pydantic/main.py", line 171, in __init__
    self.__pydantic_validator__.validate_python(data, self_instance=self)
pydantic_core._pydantic_core.ValidationError: 1 validation error for update_feed
feed_id
  Input should be a valid integer [type=int_type, input_value={'item': {'id': 47, 'titl...e': None}, 'feed_id': 1}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.6/v/int_type
2024-03-20 13:11:21,288 INFO     - product_feeds | product_feeds.one_feed_update_requested | 24badc47-c - Processed
2024-03-20 13:11:21,288 ERROR    - product_feeds | product_feeds.one_feed_update_requested | 2a82795b-7 - ValidationError: 1 validation error for update_feed
feed_id
  Input should be a valid integer [type=int_type, input_value={'item': {'id': 54, 'titl...e': None}, 'feed_id': 1}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.6/v/int_type
Traceback (most recent call last):
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/handler.py", line 367, in consume
    raise e
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/handler.py", line 331, in consume
    result = await cast(
             ^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/utils.py", line 95, in set_message_wrapper
    return await func(message)
           ^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/nats/broker.py", line 244, in process_wrapper
    r = await func(message)
        ^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/core/asynchronous.py", line 406, in decode_wrapper
    return await func(msg)
           ^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/use.py", line 146, in injected_wrapper
    r = await real_model.asolve(
        ^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/core/model.py", line 519, in asolve
    final_args, final_kwargs, call = cast_gen.send(kwargs)
                                     ^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/core/model.py", line 274, in _solve
    casted_model = self.model(**solved_kw)
                   ^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/pydantic/main.py", line 171, in __init__
    self.__pydantic_validator__.validate_python(data, self_instance=self)
pydantic_core._pydantic_core.ValidationError: 1 validation error for update_feed
feed_id
  Input should be a valid integer [type=int_type, input_value={'item': {'id': 54, 'titl...e': None}, 'feed_id': 1}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.6/v/int_type
2024-03-20 13:11:21,288 INFO     - product_feeds | product_feeds.one_feed_update_requested | 2a82795b-7 - Processed
2024-03-20 13:11:21,290 INFO     - product_feeds | product_feeds.one_feed_update_requested | 8760932d-a - Received
2024-03-20 13:11:21,290 INFO     - product_feeds | product_feeds.one_feed_update_requested | 03720de6-7 - Received
2024-03-20 13:11:21,291 INFO     - product_feeds | product_feeds.one_feed_update_requested | 23cbc2b2-4 - Received
2024-03-20 13:11:21,291 INFO     - product_feeds | product_feeds.one_feed_update_requested | 5e7e82d8-b - Received
2024-03-20 13:11:21,291 INFO     - product_feeds | product_feeds.one_feed_update_requested | 1aea43e8-7 - Received
2024-03-20 13:11:21,291 INFO     - product_feeds | product_feeds.one_feed_update_requested | 915df303-4 - Received
2024-03-20 13:11:21,291 INFO     - product_feeds | product_feeds.one_feed_update_requested | 3d36086e-f - Received
2024-03-20 13:11:21,291 INFO     - product_feeds | product_feeds.one_feed_update_requested | 88e07fba-1 - Received
2024-03-20 13:11:21,291 INFO     - product_feeds | product_feeds.one_feed_update_requested | 9f7da95e-9 - Received
2024-03-20 13:11:21,291 INFO     - product_feeds | product_feeds.one_feed_update_requested | 4e1e2a0f-2 - Received
2024-03-20 13:11:21,298 ERROR    - product_feeds | product_feeds.one_feed_update_requested | 8760932d-a - ValidationError: 1 validation error for update_feed
feed_id
  Input should be a valid integer [type=int_type, input_value={'item': {'id': 56, 'titl...e': None}, 'feed_id': 1}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.6/v/int_type
Traceback (most recent call last):
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/handler.py", line 367, in consume
    raise e
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/handler.py", line 331, in consume
    result = await cast(
             ^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/utils.py", line 95, in set_message_wrapper
    return await func(message)
           ^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/nats/broker.py", line 244, in process_wrapper
    r = await func(message)
        ^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/core/asynchronous.py", line 406, in decode_wrapper
    return await func(msg)
           ^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/use.py", line 146, in injected_wrapper
    r = await real_model.asolve(
        ^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/core/model.py", line 519, in asolve
    final_args, final_kwargs, call = cast_gen.send(kwargs)
                                     ^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/core/model.py", line 274, in _solve
    casted_model = self.model(**solved_kw)
                   ^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/pydantic/main.py", line 171, in __init__
    self.__pydantic_validator__.validate_python(data, self_instance=self)
pydantic_core._pydantic_core.ValidationError: 1 validation error for update_feed
feed_id
  Input should be a valid integer [type=int_type, input_value={'item': {'id': 56, 'titl...e': None}, 'feed_id': 1}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.6/v/int_type
2024-03-20 13:11:21,300 INFO     - product_feeds | product_feeds.one_feed_update_requested | 8760932d-a - Processed
2024-03-20 13:11:21,300 ERROR    - product_feeds | product_feeds.one_feed_update_requested | 9f7da95e-9 - ValidationError: 1 validation error for update_feed
feed_id
  Input should be a valid integer [type=int_type, input_value={'item': {'id': 64, 'titl...e': None}, 'feed_id': 1}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.6/v/int_type
Traceback (most recent call last):
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/handler.py", line 367, in consume
    raise e
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/handler.py", line 331, in consume
    result = await cast(
             ^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/utils.py", line 95, in set_message_wrapper
    return await func(message)
           ^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/nats/broker.py", line 244, in process_wrapper
    r = await func(message)
        ^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/core/asynchronous.py", line 406, in decode_wrapper
    return await func(msg)
           ^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/use.py", line 146, in injected_wrapper
    r = await real_model.asolve(
        ^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/core/model.py", line 519, in asolve
    final_args, final_kwargs, call = cast_gen.send(kwargs)
                                     ^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/core/model.py", line 274, in _solve
    casted_model = self.model(**solved_kw)
                   ^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/pydantic/main.py", line 171, in __init__
    self.__pydantic_validator__.validate_python(data, self_instance=self)
pydantic_core._pydantic_core.ValidationError: 1 validation error for update_feed
feed_id
  Input should be a valid integer [type=int_type, input_value={'item': {'id': 64, 'titl...e': None}, 'feed_id': 1}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.6/v/int_type
2024-03-20 13:11:21,301 INFO     - product_feeds | product_feeds.one_feed_update_requested | 9f7da95e-9 - Processed
2024-03-20 13:11:21,301 ERROR    - product_feeds | product_feeds.one_feed_update_requested | 1aea43e8-7 - ValidationError: 1 validation error for update_feed
feed_id
  Input should be a valid integer [type=int_type, input_value={'item': {'id': 60, 'titl...e': None}, 'feed_id': 1}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.6/v/int_type
Traceback (most recent call last):
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/handler.py", line 367, in consume
    raise e
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/handler.py", line 331, in consume
    result = await cast(
             ^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/utils.py", line 95, in set_message_wrapper
    return await func(message)
           ^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/nats/broker.py", line 244, in process_wrapper
    r = await func(message)
        ^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/core/asynchronous.py", line 406, in decode_wrapper
    return await func(msg)
           ^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/use.py", line 146, in injected_wrapper
    r = await real_model.asolve(
        ^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/core/model.py", line 519, in asolve
    final_args, final_kwargs, call = cast_gen.send(kwargs)
                                     ^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/core/model.py", line 274, in _solve
    casted_model = self.model(**solved_kw)
                   ^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/pydantic/main.py", line 171, in __init__
    self.__pydantic_validator__.validate_python(data, self_instance=self)
pydantic_core._pydantic_core.ValidationError: 1 validation error for update_feed
feed_id
  Input should be a valid integer [type=int_type, input_value={'item': {'id': 60, 'titl...e': None}, 'feed_id': 1}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.6/v/int_type
2024-03-20 13:11:21,301 INFO     - product_feeds | product_feeds.one_feed_update_requested | 1aea43e8-7 - Processed
2024-03-20 13:11:21,302 ERROR    - product_feeds | product_feeds.one_feed_update_requested | 3d36086e-f - ValidationError: 1 validation error for update_feed
feed_id
  Input should be a valid integer [type=int_type, input_value={'item': {'id': 62, 'titl...e': None}, 'feed_id': 1}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.6/v/int_type
Traceback (most recent call last):
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/handler.py", line 367, in consume
    raise e
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/handler.py", line 331, in consume
    result = await cast(
             ^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/utils.py", line 95, in set_message_wrapper
    return await func(message)
           ^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/nats/broker.py", line 244, in process_wrapper
    r = await func(message)
        ^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/core/asynchronous.py", line 406, in decode_wrapper
    return await func(msg)
           ^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/use.py", line 146, in injected_wrapper
    r = await real_model.asolve(
        ^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/core/model.py", line 519, in asolve
    final_args, final_kwargs, call = cast_gen.send(kwargs)
                                     ^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/core/model.py", line 274, in _solve
    casted_model = self.model(**solved_kw)
                   ^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/pydantic/main.py", line 171, in __init__
    self.__pydantic_validator__.validate_python(data, self_instance=self)
pydantic_core._pydantic_core.ValidationError: 1 validation error for update_feed
feed_id
  Input should be a valid integer [type=int_type, input_value={'item': {'id': 62, 'titl...e': None}, 'feed_id': 1}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.6/v/int_type
2024-03-20 13:11:21,302 INFO     - product_feeds | product_feeds.one_feed_update_requested | 3d36086e-f - Processed
2024-03-20 13:11:21,303 ERROR    - product_feeds | product_feeds.one_feed_update_requested | 5e7e82d8-b - ValidationError: 1 validation error for update_feed
feed_id
  Input should be a valid integer [type=int_type, input_value={'item': {'id': 59, 'titl...e': None}, 'feed_id': 1}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.6/v/int_type
Traceback (most recent call last):
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/handler.py", line 367, in consume
    raise e
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/handler.py", line 331, in consume
    result = await cast(
             ^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/utils.py", line 95, in set_message_wrapper
    return await func(message)
           ^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/nats/broker.py", line 244, in process_wrapper
    r = await func(message)
        ^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/core/asynchronous.py", line 406, in decode_wrapper
    return await func(msg)
           ^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/use.py", line 146, in injected_wrapper
    r = await real_model.asolve(
        ^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/core/model.py", line 519, in asolve
    final_args, final_kwargs, call = cast_gen.send(kwargs)
                                     ^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/core/model.py", line 274, in _solve
    casted_model = self.model(**solved_kw)
                   ^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/pydantic/main.py", line 171, in __init__
    self.__pydantic_validator__.validate_python(data, self_instance=self)
pydantic_core._pydantic_core.ValidationError: 1 validation error for update_feed
feed_id
  Input should be a valid integer [type=int_type, input_value={'item': {'id': 59, 'titl...e': None}, 'feed_id': 1}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.6/v/int_type
2024-03-20 13:11:21,303 INFO     - product_feeds | product_feeds.one_feed_update_requested | 5e7e82d8-b - Processed
2024-03-20 13:11:21,304 ERROR    - product_feeds | product_feeds.one_feed_update_requested | 915df303-4 - ValidationError: 1 validation error for update_feed
feed_id
  Input should be a valid integer [type=int_type, input_value={'item': {'id': 61, 'titl...e': None}, 'feed_id': 1}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.6/v/int_type
Traceback (most recent call last):
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/handler.py", line 367, in consume
    raise e
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/handler.py", line 331, in consume
    result = await cast(
             ^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/utils.py", line 95, in set_message_wrapper
    return await func(message)
           ^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/nats/broker.py", line 244, in process_wrapper
    r = await func(message)
        ^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/core/asynchronous.py", line 406, in decode_wrapper
    return await func(msg)
           ^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/use.py", line 146, in injected_wrapper
    r = await real_model.asolve(
        ^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/core/model.py", line 519, in asolve
    final_args, final_kwargs, call = cast_gen.send(kwargs)
                                     ^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/core/model.py", line 274, in _solve
    casted_model = self.model(**solved_kw)
                   ^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/pydantic/main.py", line 171, in __init__
    self.__pydantic_validator__.validate_python(data, self_instance=self)
pydantic_core._pydantic_core.ValidationError: 1 validation error for update_feed
feed_id
  Input should be a valid integer [type=int_type, input_value={'item': {'id': 61, 'titl...e': None}, 'feed_id': 1}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.6/v/int_type
2024-03-20 13:11:21,304 INFO     - product_feeds | product_feeds.one_feed_update_requested | 915df303-4 - Processed
2024-03-20 13:11:21,305 ERROR    - product_feeds | product_feeds.one_feed_update_requested | 88e07fba-1 - ValidationError: 1 validation error for update_feed
feed_id
  Input should be a valid integer [type=int_type, input_value={'item': {'id': 63, 'titl...e': None}, 'feed_id': 1}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.6/v/int_type
Traceback (most recent call last):
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/handler.py", line 367, in consume
    raise e
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/handler.py", line 331, in consume
    result = await cast(
             ^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/utils.py", line 95, in set_message_wrapper
    return await func(message)
           ^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/nats/broker.py", line 244, in process_wrapper
    r = await func(message)
        ^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/core/asynchronous.py", line 406, in decode_wrapper
    return await func(msg)
           ^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/use.py", line 146, in injected_wrapper
    r = await real_model.asolve(
        ^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/core/model.py", line 519, in asolve
    final_args, final_kwargs, call = cast_gen.send(kwargs)
                                     ^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/core/model.py", line 274, in _solve
    casted_model = self.model(**solved_kw)
                   ^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/pydantic/main.py", line 171, in __init__
    self.__pydantic_validator__.validate_python(data, self_instance=self)
pydantic_core._pydantic_core.ValidationError: 1 validation error for update_feed
feed_id
  Input should be a valid integer [type=int_type, input_value={'item': {'id': 63, 'titl...e': None}, 'feed_id': 1}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.6/v/int_type
2024-03-20 13:11:21,305 INFO     - product_feeds | product_feeds.one_feed_update_requested | 88e07fba-1 - Processed
2024-03-20 13:11:21,305 ERROR    - product_feeds | product_feeds.one_feed_update_requested | 23cbc2b2-4 - ValidationError: 1 validation error for update_feed
feed_id
  Input should be a valid integer [type=int_type, input_value={'item': {'id': 58, 'titl...e': None}, 'feed_id': 1}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.6/v/int_type
Traceback (most recent call last):
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/handler.py", line 367, in consume
    raise e
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/handler.py", line 331, in consume
    result = await cast(
             ^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/utils.py", line 95, in set_message_wrapper
    return await func(message)
           ^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/nats/broker.py", line 244, in process_wrapper
    r = await func(message)
        ^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/core/asynchronous.py", line 406, in decode_wrapper
    return await func(msg)
           ^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/use.py", line 146, in injected_wrapper
    r = await real_model.asolve(
        ^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/core/model.py", line 519, in asolve
    final_args, final_kwargs, call = cast_gen.send(kwargs)
                                     ^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/core/model.py", line 274, in _solve
    casted_model = self.model(**solved_kw)
                   ^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/pydantic/main.py", line 171, in __init__
    self.__pydantic_validator__.validate_python(data, self_instance=self)
pydantic_core._pydantic_core.ValidationError: 1 validation error for update_feed
feed_id
  Input should be a valid integer [type=int_type, input_value={'item': {'id': 58, 'titl...e': None}, 'feed_id': 1}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.6/v/int_type
2024-03-20 13:11:21,306 INFO     - product_feeds | product_feeds.one_feed_update_requested | 23cbc2b2-4 - Processed
2024-03-20 13:11:21,306 ERROR    - product_feeds | product_feeds.one_feed_update_requested | 4e1e2a0f-2 - ValidationError: 1 validation error for update_feed
feed_id
  Input should be a valid integer [type=int_type, input_value={'item': {'id': 65, 'titl...e': None}, 'feed_id': 1}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.6/v/int_type
Traceback (most recent call last):
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/handler.py", line 367, in consume
    raise e
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/handler.py", line 331, in consume
    result = await cast(
             ^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/utils.py", line 95, in set_message_wrapper
    return await func(message)
           ^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/nats/broker.py", line 244, in process_wrapper
    r = await func(message)
        ^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/core/asynchronous.py", line 406, in decode_wrapper
    return await func(msg)
           ^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/use.py", line 146, in injected_wrapper
    r = await real_model.asolve(
        ^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/core/model.py", line 519, in asolve
    final_args, final_kwargs, call = cast_gen.send(kwargs)
                                     ^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/core/model.py", line 274, in _solve
    casted_model = self.model(**solved_kw)
                   ^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/pydantic/main.py", line 171, in __init__
    self.__pydantic_validator__.validate_python(data, self_instance=self)
pydantic_core._pydantic_core.ValidationError: 1 validation error for update_feed
feed_id
  Input should be a valid integer [type=int_type, input_value={'item': {'id': 65, 'titl...e': None}, 'feed_id': 1}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.6/v/int_type
2024-03-20 13:11:21,307 INFO     - product_feeds | product_feeds.one_feed_update_requested | 4e1e2a0f-2 - Processed
2024-03-20 13:11:21,307 ERROR    - product_feeds | product_feeds.one_feed_update_requested | 03720de6-7 - ValidationError: 1 validation error for update_feed
feed_id
  Input should be a valid integer [type=int_type, input_value={'item': {'id': 57, 'titl...e': None}, 'feed_id': 1}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.6/v/int_type
Traceback (most recent call last):
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/handler.py", line 367, in consume
    raise e
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/handler.py", line 331, in consume
    result = await cast(
             ^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/utils.py", line 95, in set_message_wrapper
    return await func(message)
           ^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/nats/broker.py", line 244, in process_wrapper
    r = await func(message)
        ^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/core/asynchronous.py", line 406, in decode_wrapper
    return await func(msg)
           ^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/use.py", line 146, in injected_wrapper
    r = await real_model.asolve(
        ^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/core/model.py", line 519, in asolve
    final_args, final_kwargs, call = cast_gen.send(kwargs)
                                     ^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/core/model.py", line 274, in _solve
    casted_model = self.model(**solved_kw)
                   ^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/pydantic/main.py", line 171, in __init__
    self.__pydantic_validator__.validate_python(data, self_instance=self)
pydantic_core._pydantic_core.ValidationError: 1 validation error for update_feed
feed_id
  Input should be a valid integer [type=int_type, input_value={'item': {'id': 57, 'titl...e': None}, 'feed_id': 1}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.6/v/int_type
2024-03-20 13:11:21,308 INFO     - product_feeds | product_feeds.one_feed_update_requested | 03720de6-7 - Processed
2024-03-20 13:11:21,310 INFO     - product_feeds | product_feeds.one_feed_update_requested | 7e221313-9 - Received
2024-03-20 13:11:21,310 INFO     - product_feeds | product_feeds.one_feed_update_requested | 45705d79-2 - Received
2024-03-20 13:11:21,310 INFO     - product_feeds | product_feeds.one_feed_update_requested | b15258fa-2 - Received
2024-03-20 13:11:21,310 INFO     - product_feeds | product_feeds.one_feed_update_requested | 87c2ea2f-9 - Received
2024-03-20 13:11:21,310 INFO     - product_feeds | product_feeds.one_feed_update_requested | 0caea681-2 - Received
2024-03-20 13:11:21,310 INFO     - product_feeds | product_feeds.one_feed_update_requested | c398345f-9 - Received
2024-03-20 13:11:21,310 INFO     - product_feeds | product_feeds.one_feed_update_requested | 41758bde-b - Received
2024-03-20 13:11:21,310 INFO     - product_feeds | product_feeds.one_feed_update_requested | 25fa4e4c-c - Received
2024-03-20 13:11:21,311 INFO     - product_feeds | product_feeds.one_feed_update_requested | c5e9aa42-7 - Received
2024-03-20 13:11:21,311 INFO     - product_feeds | product_feeds.one_feed_update_requested | 66b07c44-e - Received
2024-03-20 13:11:21,313 ERROR    - product_feeds | product_feeds.one_feed_update_requested | 7e221313-9 - ValidationError: 1 validation error for update_feed
feed_id
  Input should be a valid integer [type=int_type, input_value={'item': {'id': 66, 'titl...e': None}, 'feed_id': 1}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.6/v/int_type
Traceback (most recent call last):
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/handler.py", line 367, in consume
    raise e
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/handler.py", line 331, in consume
    result = await cast(
             ^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/utils.py", line 95, in set_message_wrapper
    return await func(message)
           ^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/nats/broker.py", line 244, in process_wrapper
    r = await func(message)
        ^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/core/asynchronous.py", line 406, in decode_wrapper
    return await func(msg)
           ^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/use.py", line 146, in injected_wrapper
    r = await real_model.asolve(
        ^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/core/model.py", line 519, in asolve
    final_args, final_kwargs, call = cast_gen.send(kwargs)
                                     ^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/core/model.py", line 274, in _solve
    casted_model = self.model(**solved_kw)
                   ^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/pydantic/main.py", line 171, in __init__
    self.__pydantic_validator__.validate_python(data, self_instance=self)
pydantic_core._pydantic_core.ValidationError: 1 validation error for update_feed
feed_id
  Input should be a valid integer [type=int_type, input_value={'item': {'id': 66, 'titl...e': None}, 'feed_id': 1}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.6/v/int_type
2024-03-20 13:11:21,322 INFO     - product_feeds | product_feeds.one_feed_update_requested | 7e221313-9 - Processed
2024-03-20 13:11:21,323 ERROR    - product_feeds | product_feeds.one_feed_update_requested | 0caea681-2 - ValidationError: 1 validation error for update_feed
feed_id
  Input should be a valid integer [type=int_type, input_value={'item': {'id': 70, 'titl...e': None}, 'feed_id': 1}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.6/v/int_type
Traceback (most recent call last):
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/handler.py", line 367, in consume
    raise e
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/handler.py", line 331, in consume
    result = await cast(
             ^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/utils.py", line 95, in set_message_wrapper
    return await func(message)
           ^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/nats/broker.py", line 244, in process_wrapper
    r = await func(message)
        ^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/core/asynchronous.py", line 406, in decode_wrapper
    return await func(msg)
           ^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/use.py", line 146, in injected_wrapper
    r = await real_model.asolve(
        ^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/core/model.py", line 519, in asolve
    final_args, final_kwargs, call = cast_gen.send(kwargs)
                                     ^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/core/model.py", line 274, in _solve
    casted_model = self.model(**solved_kw)
                   ^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/pydantic/main.py", line 171, in __init__
    self.__pydantic_validator__.validate_python(data, self_instance=self)
pydantic_core._pydantic_core.ValidationError: 1 validation error for update_feed
feed_id
  Input should be a valid integer [type=int_type, input_value={'item': {'id': 70, 'titl...e': None}, 'feed_id': 1}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.6/v/int_type
2024-03-20 13:11:21,324 INFO     - product_feeds | product_feeds.one_feed_update_requested | 0caea681-2 - Processed
2024-03-20 13:11:21,324 ERROR    - product_feeds | product_feeds.one_feed_update_requested | b15258fa-2 - ValidationError: 1 validation error for update_feed
feed_id
  Input should be a valid integer [type=int_type, input_value={'item': {'id': 68, 'titl...e': None}, 'feed_id': 1}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.6/v/int_type
Traceback (most recent call last):
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/handler.py", line 367, in consume
    raise e
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/handler.py", line 331, in consume
    result = await cast(
             ^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/utils.py", line 95, in set_message_wrapper
    return await func(message)
           ^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/nats/broker.py", line 244, in process_wrapper
    r = await func(message)
        ^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/core/asynchronous.py", line 406, in decode_wrapper
    return await func(msg)
           ^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/use.py", line 146, in injected_wrapper
    r = await real_model.asolve(
        ^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/core/model.py", line 519, in asolve
    final_args, final_kwargs, call = cast_gen.send(kwargs)
                                     ^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/core/model.py", line 274, in _solve
    casted_model = self.model(**solved_kw)
                   ^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/pydantic/main.py", line 171, in __init__
    self.__pydantic_validator__.validate_python(data, self_instance=self)
pydantic_core._pydantic_core.ValidationError: 1 validation error for update_feed
feed_id
  Input should be a valid integer [type=int_type, input_value={'item': {'id': 68, 'titl...e': None}, 'feed_id': 1}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.6/v/int_type
2024-03-20 13:11:21,325 INFO     - product_feeds | product_feeds.one_feed_update_requested | b15258fa-2 - Processed
2024-03-20 13:11:21,325 ERROR    - product_feeds | product_feeds.one_feed_update_requested | 66b07c44-e - ValidationError: 1 validation error for update_feed
feed_id
  Input should be a valid integer [type=int_type, input_value={'item': {'id': 75, 'titl...e': None}, 'feed_id': 1}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.6/v/int_type
Traceback (most recent call last):
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/handler.py", line 367, in consume
    raise e
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/handler.py", line 331, in consume
    result = await cast(
             ^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/utils.py", line 95, in set_message_wrapper
    return await func(message)
           ^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/nats/broker.py", line 244, in process_wrapper
    r = await func(message)
        ^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/core/asynchronous.py", line 406, in decode_wrapper
    return await func(msg)
           ^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/use.py", line 146, in injected_wrapper
    r = await real_model.asolve(
        ^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/core/model.py", line 519, in asolve
    final_args, final_kwargs, call = cast_gen.send(kwargs)
                                     ^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/core/model.py", line 274, in _solve
    casted_model = self.model(**solved_kw)
                   ^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/pydantic/main.py", line 171, in __init__
    self.__pydantic_validator__.validate_python(data, self_instance=self)
pydantic_core._pydantic_core.ValidationError: 1 validation error for update_feed
feed_id
  Input should be a valid integer [type=int_type, input_value={'item': {'id': 75, 'titl...e': None}, 'feed_id': 1}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.6/v/int_type
2024-03-20 13:11:21,326 INFO     - product_feeds | product_feeds.one_feed_update_requested | 66b07c44-e - Processed
2024-03-20 13:11:21,326 ERROR    - product_feeds | product_feeds.one_feed_update_requested | 41758bde-b - ValidationError: 1 validation error for update_feed
feed_id
  Input should be a valid integer [type=int_type, input_value={'item': {'id': 72, 'titl...e': None}, 'feed_id': 1}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.6/v/int_type
Traceback (most recent call last):
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/handler.py", line 367, in consume
    raise e
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/handler.py", line 331, in consume
    result = await cast(
             ^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/utils.py", line 95, in set_message_wrapper
    return await func(message)
           ^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/nats/broker.py", line 244, in process_wrapper
    r = await func(message)
        ^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/core/asynchronous.py", line 406, in decode_wrapper
    return await func(msg)
           ^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/use.py", line 146, in injected_wrapper
    r = await real_model.asolve(
        ^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/core/model.py", line 519, in asolve
    final_args, final_kwargs, call = cast_gen.send(kwargs)
                                     ^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/core/model.py", line 274, in _solve
    casted_model = self.model(**solved_kw)
                   ^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/pydantic/main.py", line 171, in __init__
    self.__pydantic_validator__.validate_python(data, self_instance=self)
pydantic_core._pydantic_core.ValidationError: 1 validation error for update_feed
feed_id
  Input should be a valid integer [type=int_type, input_value={'item': {'id': 72, 'titl...e': None}, 'feed_id': 1}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.6/v/int_type
2024-03-20 13:11:21,326 INFO     - product_feeds | product_feeds.one_feed_update_requested | 41758bde-b - Processed
2024-03-20 13:11:21,326 ERROR    - product_feeds | product_feeds.one_feed_update_requested | 25fa4e4c-c - ValidationError: 1 validation error for update_feed
feed_id
  Input should be a valid integer [type=int_type, input_value={'item': {'id': 73, 'titl...e': None}, 'feed_id': 1}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.6/v/int_type
Traceback (most recent call last):
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/handler.py", line 367, in consume
    raise e
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/handler.py", line 331, in consume
    result = await cast(
             ^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/utils.py", line 95, in set_message_wrapper
    return await func(message)
           ^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/nats/broker.py", line 244, in process_wrapper
    r = await func(message)
        ^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/core/asynchronous.py", line 406, in decode_wrapper
    return await func(msg)
           ^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/use.py", line 146, in injected_wrapper
    r = await real_model.asolve(
        ^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/core/model.py", line 519, in asolve
    final_args, final_kwargs, call = cast_gen.send(kwargs)
                                     ^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/core/model.py", line 274, in _solve
    casted_model = self.model(**solved_kw)
                   ^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/pydantic/main.py", line 171, in __init__
    self.__pydantic_validator__.validate_python(data, self_instance=self)
pydantic_core._pydantic_core.ValidationError: 1 validation error for update_feed
feed_id
  Input should be a valid integer [type=int_type, input_value={'item': {'id': 73, 'titl...e': None}, 'feed_id': 1}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.6/v/int_type
2024-03-20 13:11:21,327 INFO     - product_feeds | product_feeds.one_feed_update_requested | 25fa4e4c-c - Processed
2024-03-20 13:11:21,328 ERROR    - product_feeds | product_feeds.one_feed_update_requested | c5e9aa42-7 - ValidationError: 1 validation error for update_feed
feed_id
  Input should be a valid integer [type=int_type, input_value={'item': {'id': 74, 'titl...e': None}, 'feed_id': 1}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.6/v/int_type
Traceback (most recent call last):
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/handler.py", line 367, in consume
    raise e
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/handler.py", line 331, in consume
    result = await cast(
             ^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/utils.py", line 95, in set_message_wrapper
    return await func(message)
           ^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/nats/broker.py", line 244, in process_wrapper
    r = await func(message)
        ^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/core/asynchronous.py", line 406, in decode_wrapper
    return await func(msg)
           ^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/use.py", line 146, in injected_wrapper
    r = await real_model.asolve(
        ^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/core/model.py", line 519, in asolve
    final_args, final_kwargs, call = cast_gen.send(kwargs)
                                     ^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/core/model.py", line 274, in _solve
    casted_model = self.model(**solved_kw)
                   ^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/pydantic/main.py", line 171, in __init__
    self.__pydantic_validator__.validate_python(data, self_instance=self)
pydantic_core._pydantic_core.ValidationError: 1 validation error for update_feed
feed_id
  Input should be a valid integer [type=int_type, input_value={'item': {'id': 74, 'titl...e': None}, 'feed_id': 1}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.6/v/int_type
2024-03-20 13:11:21,328 INFO     - product_feeds | product_feeds.one_feed_update_requested | c5e9aa42-7 - Processed
2024-03-20 13:11:21,329 ERROR    - product_feeds | product_feeds.one_feed_update_requested | c398345f-9 - ValidationError: 1 validation error for update_feed
feed_id
  Input should be a valid integer [type=int_type, input_value={'item': {'id': 71, 'titl...e': None}, 'feed_id': 1}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.6/v/int_type
Traceback (most recent call last):
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/handler.py", line 367, in consume
    raise e
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/handler.py", line 331, in consume
    result = await cast(
             ^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/utils.py", line 95, in set_message_wrapper
    return await func(message)
           ^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/nats/broker.py", line 244, in process_wrapper
    r = await func(message)
        ^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/core/asynchronous.py", line 406, in decode_wrapper
    return await func(msg)
           ^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/use.py", line 146, in injected_wrapper
    r = await real_model.asolve(
        ^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/core/model.py", line 519, in asolve
    final_args, final_kwargs, call = cast_gen.send(kwargs)
                                     ^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/core/model.py", line 274, in _solve
    casted_model = self.model(**solved_kw)
                   ^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/pydantic/main.py", line 171, in __init__
    self.__pydantic_validator__.validate_python(data, self_instance=self)
pydantic_core._pydantic_core.ValidationError: 1 validation error for update_feed
feed_id
  Input should be a valid integer [type=int_type, input_value={'item': {'id': 71, 'titl...e': None}, 'feed_id': 1}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.6/v/int_type
2024-03-20 13:11:21,329 INFO     - product_feeds | product_feeds.one_feed_update_requested | c398345f-9 - Processed
2024-03-20 13:11:21,330 ERROR    - product_feeds | product_feeds.one_feed_update_requested | 87c2ea2f-9 - ValidationError: 1 validation error for update_feed
feed_id
  Input should be a valid integer [type=int_type, input_value={'item': {'id': 69, 'titl...e': None}, 'feed_id': 1}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.6/v/int_type
Traceback (most recent call last):
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/handler.py", line 367, in consume
    raise e
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/handler.py", line 331, in consume
    result = await cast(
             ^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/utils.py", line 95, in set_message_wrapper
    return await func(message)
           ^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/nats/broker.py", line 244, in process_wrapper
    r = await func(message)
        ^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/core/asynchronous.py", line 406, in decode_wrapper
    return await func(msg)
           ^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/use.py", line 146, in injected_wrapper
    r = await real_model.asolve(
        ^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/core/model.py", line 519, in asolve
    final_args, final_kwargs, call = cast_gen.send(kwargs)
                                     ^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/core/model.py", line 274, in _solve
    casted_model = self.model(**solved_kw)
                   ^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/pydantic/main.py", line 171, in __init__
    self.__pydantic_validator__.validate_python(data, self_instance=self)
pydantic_core._pydantic_core.ValidationError: 1 validation error for update_feed
feed_id
  Input should be a valid integer [type=int_type, input_value={'item': {'id': 69, 'titl...e': None}, 'feed_id': 1}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.6/v/int_type
2024-03-20 13:11:21,330 INFO     - product_feeds | product_feeds.one_feed_update_requested | 87c2ea2f-9 - Processed
2024-03-20 13:11:21,330 ERROR    - product_feeds | product_feeds.one_feed_update_requested | 45705d79-2 - ValidationError: 1 validation error for update_feed
feed_id
  Input should be a valid integer [type=int_type, input_value={'item': {'id': 67, 'titl...e': None}, 'feed_id': 1}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.6/v/int_type
Traceback (most recent call last):
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/handler.py", line 367, in consume
    raise e
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/handler.py", line 331, in consume
    result = await cast(
             ^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/utils.py", line 95, in set_message_wrapper
    return await func(message)
           ^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/nats/broker.py", line 244, in process_wrapper
    r = await func(message)
        ^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/core/asynchronous.py", line 406, in decode_wrapper
    return await func(msg)
           ^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/use.py", line 146, in injected_wrapper
    r = await real_model.asolve(
        ^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/core/model.py", line 519, in asolve
    final_args, final_kwargs, call = cast_gen.send(kwargs)
                                     ^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/core/model.py", line 274, in _solve
    casted_model = self.model(**solved_kw)
                   ^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/pydantic/main.py", line 171, in __init__
    self.__pydantic_validator__.validate_python(data, self_instance=self)
pydantic_core._pydantic_core.ValidationError: 1 validation error for update_feed
feed_id
  Input should be a valid integer [type=int_type, input_value={'item': {'id': 67, 'titl...e': None}, 'feed_id': 1}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.6/v/int_type
2024-03-20 13:11:21,331 INFO     - product_feeds | product_feeds.one_feed_update_requested | 45705d79-2 - Processed
2024-03-20 13:11:21,334 INFO     - product_feeds | product_feeds.one_feed_update_requested | 3f92e1ba-2 - Received
2024-03-20 13:11:21,334 INFO     - product_feeds | product_feeds.one_feed_update_requested | e9b625b6-f - Received
2024-03-20 13:11:21,334 INFO     - product_feeds | product_feeds.one_feed_update_requested | 69ca5f80-3 - Received
2024-03-20 13:11:21,334 INFO     - product_feeds | product_feeds.one_feed_update_requested | a24d6fc2-e - Received
2024-03-20 13:11:21,334 INFO     - product_feeds | product_feeds.one_feed_update_requested | ba9b2bba-1 - Received
2024-03-20 13:11:21,334 INFO     - product_feeds | product_feeds.one_feed_update_requested | af5ca1b6-8 - Received
2024-03-20 13:11:21,334 INFO     - product_feeds | product_feeds.one_feed_update_requested | d5fc82ec-e - Received
2024-03-20 13:11:21,334 INFO     - product_feeds | product_feeds.one_feed_update_requested | c7c48c67-d - Received
2024-03-20 13:11:21,334 INFO     - product_feeds | product_feeds.one_feed_update_requested | edeca42b-7 - Received
2024-03-20 13:11:21,334 INFO     - product_feeds | product_feeds.one_feed_update_requested | 4ef3cf91-4 - Received
2024-03-20 13:11:21,343 ERROR    - product_feeds | product_feeds.one_feed_update_requested | af5ca1b6-8 - ValidationError: 1 validation error for update_feed
feed_id
  Input should be a valid integer [type=int_type, input_value={'item': {'id': 81, 'titl...e': None}, 'feed_id': 1}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.6/v/int_type
Traceback (most recent call last):
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/handler.py", line 367, in consume
    raise e
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/handler.py", line 331, in consume
    result = await cast(
             ^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/utils.py", line 95, in set_message_wrapper
    return await func(message)
           ^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/nats/broker.py", line 244, in process_wrapper
    r = await func(message)
        ^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/core/asynchronous.py", line 406, in decode_wrapper
    return await func(msg)
           ^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/use.py", line 146, in injected_wrapper
    r = await real_model.asolve(
        ^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/core/model.py", line 519, in asolve
    final_args, final_kwargs, call = cast_gen.send(kwargs)
                                     ^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/core/model.py", line 274, in _solve
    casted_model = self.model(**solved_kw)
                   ^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/pydantic/main.py", line 171, in __init__
    self.__pydantic_validator__.validate_python(data, self_instance=self)
pydantic_core._pydantic_core.ValidationError: 1 validation error for update_feed
feed_id
  Input should be a valid integer [type=int_type, input_value={'item': {'id': 81, 'titl...e': None}, 'feed_id': 1}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.6/v/int_type
2024-03-20 13:11:21,344 INFO     - product_feeds | product_feeds.one_feed_update_requested | af5ca1b6-8 - Processed
2024-03-20 13:11:21,344 ERROR    - product_feeds | product_feeds.one_feed_update_requested | c7c48c67-d - ValidationError: 1 validation error for update_feed
feed_id
  Input should be a valid integer [type=int_type, input_value={'item': {'id': 83, 'titl...e': None}, 'feed_id': 1}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.6/v/int_type
Traceback (most recent call last):
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/handler.py", line 367, in consume
    raise e
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/handler.py", line 331, in consume
    result = await cast(
             ^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/utils.py", line 95, in set_message_wrapper
    return await func(message)
           ^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/nats/broker.py", line 244, in process_wrapper
    r = await func(message)
        ^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/core/asynchronous.py", line 406, in decode_wrapper
    return await func(msg)
           ^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/use.py", line 146, in injected_wrapper
    r = await real_model.asolve(
        ^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/core/model.py", line 519, in asolve
    final_args, final_kwargs, call = cast_gen.send(kwargs)
                                     ^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/core/model.py", line 274, in _solve
    casted_model = self.model(**solved_kw)
                   ^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/pydantic/main.py", line 171, in __init__
    self.__pydantic_validator__.validate_python(data, self_instance=self)
pydantic_core._pydantic_core.ValidationError: 1 validation error for update_feed
feed_id
  Input should be a valid integer [type=int_type, input_value={'item': {'id': 83, 'titl...e': None}, 'feed_id': 1}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.6/v/int_type
2024-03-20 13:11:21,345 INFO     - product_feeds | product_feeds.one_feed_update_requested | c7c48c67-d - Processed
2024-03-20 13:11:21,345 ERROR    - product_feeds | product_feeds.one_feed_update_requested | e9b625b6-f - ValidationError: 1 validation error for update_feed
feed_id
  Input should be a valid integer [type=int_type, input_value={'item': {'id': 77, 'titl...e': None}, 'feed_id': 1}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.6/v/int_type
Traceback (most recent call last):
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/handler.py", line 367, in consume
    raise e
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/handler.py", line 331, in consume
    result = await cast(
             ^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/utils.py", line 95, in set_message_wrapper
    return await func(message)
           ^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/nats/broker.py", line 244, in process_wrapper
    r = await func(message)
        ^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/core/asynchronous.py", line 406, in decode_wrapper
    return await func(msg)
           ^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/use.py", line 146, in injected_wrapper
    r = await real_model.asolve(
        ^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/core/model.py", line 519, in asolve
    final_args, final_kwargs, call = cast_gen.send(kwargs)
                                     ^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/core/model.py", line 274, in _solve
    casted_model = self.model(**solved_kw)
                   ^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/pydantic/main.py", line 171, in __init__
    self.__pydantic_validator__.validate_python(data, self_instance=self)
pydantic_core._pydantic_core.ValidationError: 1 validation error for update_feed
feed_id
  Input should be a valid integer [type=int_type, input_value={'item': {'id': 77, 'titl...e': None}, 'feed_id': 1}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.6/v/int_type
2024-03-20 13:11:21,346 INFO     - product_feeds | product_feeds.one_feed_update_requested | e9b625b6-f - Processed
2024-03-20 13:11:21,346 ERROR    - product_feeds | product_feeds.one_feed_update_requested | 4ef3cf91-4 - ValidationError: 1 validation error for update_feed
feed_id
  Input should be a valid integer [type=int_type, input_value={'item': {'id': 85, 'titl...e': None}, 'feed_id': 1}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.6/v/int_type
Traceback (most recent call last):
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/handler.py", line 367, in consume
    raise e
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/handler.py", line 331, in consume
    result = await cast(
             ^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/utils.py", line 95, in set_message_wrapper
    return await func(message)
           ^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/nats/broker.py", line 244, in process_wrapper
    r = await func(message)
        ^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/core/asynchronous.py", line 406, in decode_wrapper
    return await func(msg)
           ^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/use.py", line 146, in injected_wrapper
    r = await real_model.asolve(
        ^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/core/model.py", line 519, in asolve
    final_args, final_kwargs, call = cast_gen.send(kwargs)
                                     ^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/core/model.py", line 274, in _solve
    casted_model = self.model(**solved_kw)
                   ^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/pydantic/main.py", line 171, in __init__
    self.__pydantic_validator__.validate_python(data, self_instance=self)
pydantic_core._pydantic_core.ValidationError: 1 validation error for update_feed
feed_id
  Input should be a valid integer [type=int_type, input_value={'item': {'id': 85, 'titl...e': None}, 'feed_id': 1}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.6/v/int_type
2024-03-20 13:11:21,347 INFO     - product_feeds | product_feeds.one_feed_update_requested | 4ef3cf91-4 - Processed
2024-03-20 13:11:21,348 ERROR    - product_feeds | product_feeds.one_feed_update_requested | ba9b2bba-1 - ValidationError: 1 validation error for update_feed
feed_id
  Input should be a valid integer [type=int_type, input_value={'item': {'id': 80, 'titl...e': None}, 'feed_id': 1}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.6/v/int_type
Traceback (most recent call last):
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/handler.py", line 367, in consume
    raise e
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/handler.py", line 331, in consume
    result = await cast(
             ^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/utils.py", line 95, in set_message_wrapper
    return await func(message)
           ^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/nats/broker.py", line 244, in process_wrapper
    r = await func(message)
        ^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/core/asynchronous.py", line 406, in decode_wrapper
    return await func(msg)
           ^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/use.py", line 146, in injected_wrapper
    r = await real_model.asolve(
        ^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/core/model.py", line 519, in asolve
    final_args, final_kwargs, call = cast_gen.send(kwargs)
                                     ^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/core/model.py", line 274, in _solve
    casted_model = self.model(**solved_kw)
                   ^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/pydantic/main.py", line 171, in __init__
    self.__pydantic_validator__.validate_python(data, self_instance=self)
pydantic_core._pydantic_core.ValidationError: 1 validation error for update_feed
feed_id
  Input should be a valid integer [type=int_type, input_value={'item': {'id': 80, 'titl...e': None}, 'feed_id': 1}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.6/v/int_type
2024-03-20 13:11:21,348 INFO     - product_feeds | product_feeds.one_feed_update_requested | ba9b2bba-1 - Processed
2024-03-20 13:11:21,349 ERROR    - product_feeds | product_feeds.one_feed_update_requested | a24d6fc2-e - ValidationError: 1 validation error for update_feed
feed_id
  Input should be a valid integer [type=int_type, input_value={'item': {'id': 79, 'titl...e': None}, 'feed_id': 1}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.6/v/int_type
Traceback (most recent call last):
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/handler.py", line 367, in consume
    raise e
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/handler.py", line 331, in consume
    result = await cast(
             ^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/utils.py", line 95, in set_message_wrapper
    return await func(message)
           ^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/nats/broker.py", line 244, in process_wrapper
    r = await func(message)
        ^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/core/asynchronous.py", line 406, in decode_wrapper
    return await func(msg)
           ^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/use.py", line 146, in injected_wrapper
    r = await real_model.asolve(
        ^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/core/model.py", line 519, in asolve
    final_args, final_kwargs, call = cast_gen.send(kwargs)
                                     ^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/core/model.py", line 274, in _solve
    casted_model = self.model(**solved_kw)
                   ^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/pydantic/main.py", line 171, in __init__
    self.__pydantic_validator__.validate_python(data, self_instance=self)
pydantic_core._pydantic_core.ValidationError: 1 validation error for update_feed
feed_id
  Input should be a valid integer [type=int_type, input_value={'item': {'id': 79, 'titl...e': None}, 'feed_id': 1}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.6/v/int_type
2024-03-20 13:11:21,350 INFO     - product_feeds | product_feeds.one_feed_update_requested | a24d6fc2-e - Processed
2024-03-20 13:11:21,350 ERROR    - product_feeds | product_feeds.one_feed_update_requested | edeca42b-7 - ValidationError: 1 validation error for update_feed
feed_id
  Input should be a valid integer [type=int_type, input_value={'item': {'id': 84, 'titl...e': None}, 'feed_id': 1}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.6/v/int_type
Traceback (most recent call last):
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/handler.py", line 367, in consume
    raise e
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/handler.py", line 331, in consume
    result = await cast(
             ^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/utils.py", line 95, in set_message_wrapper
    return await func(message)
           ^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/nats/broker.py", line 244, in process_wrapper
    r = await func(message)
        ^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/core/asynchronous.py", line 406, in decode_wrapper
    return await func(msg)
           ^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/use.py", line 146, in injected_wrapper
    r = await real_model.asolve(
        ^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/core/model.py", line 519, in asolve
    final_args, final_kwargs, call = cast_gen.send(kwargs)
                                     ^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/core/model.py", line 274, in _solve
    casted_model = self.model(**solved_kw)
                   ^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/pydantic/main.py", line 171, in __init__
    self.__pydantic_validator__.validate_python(data, self_instance=self)
pydantic_core._pydantic_core.ValidationError: 1 validation error for update_feed
feed_id
  Input should be a valid integer [type=int_type, input_value={'item': {'id': 84, 'titl...e': None}, 'feed_id': 1}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.6/v/int_type
2024-03-20 13:11:21,351 INFO     - product_feeds | product_feeds.one_feed_update_requested | edeca42b-7 - Processed
2024-03-20 13:11:21,351 ERROR    - product_feeds | product_feeds.one_feed_update_requested | d5fc82ec-e - ValidationError: 1 validation error for update_feed
feed_id
  Input should be a valid integer [type=int_type, input_value={'item': {'id': 82, 'titl...e': None}, 'feed_id': 1}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.6/v/int_type
Traceback (most recent call last):
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/handler.py", line 367, in consume
    raise e
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/handler.py", line 331, in consume
    result = await cast(
             ^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/utils.py", line 95, in set_message_wrapper
    return await func(message)
           ^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/nats/broker.py", line 244, in process_wrapper
    r = await func(message)
        ^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/core/asynchronous.py", line 406, in decode_wrapper
    return await func(msg)
           ^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/use.py", line 146, in injected_wrapper
    r = await real_model.asolve(
        ^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/core/model.py", line 519, in asolve
    final_args, final_kwargs, call = cast_gen.send(kwargs)
                                     ^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/core/model.py", line 274, in _solve
    casted_model = self.model(**solved_kw)
                   ^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/pydantic/main.py", line 171, in __init__
    self.__pydantic_validator__.validate_python(data, self_instance=self)
pydantic_core._pydantic_core.ValidationError: 1 validation error for update_feed
feed_id
  Input should be a valid integer [type=int_type, input_value={'item': {'id': 82, 'titl...e': None}, 'feed_id': 1}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.6/v/int_type
2024-03-20 13:11:21,352 INFO     - product_feeds | product_feeds.one_feed_update_requested | d5fc82ec-e - Processed
2024-03-20 13:11:21,352 ERROR    - product_feeds | product_feeds.one_feed_update_requested | 69ca5f80-3 - ValidationError: 1 validation error for update_feed
feed_id
  Input should be a valid integer [type=int_type, input_value={'item': {'id': 78, 'titl...e': None}, 'feed_id': 1}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.6/v/int_type
Traceback (most recent call last):
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/handler.py", line 367, in consume
    raise e
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/handler.py", line 331, in consume
    result = await cast(
             ^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/utils.py", line 95, in set_message_wrapper
    return await func(message)
           ^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/nats/broker.py", line 244, in process_wrapper
    r = await func(message)
        ^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/core/asynchronous.py", line 406, in decode_wrapper
    return await func(msg)
           ^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/use.py", line 146, in injected_wrapper
    r = await real_model.asolve(
        ^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/core/model.py", line 519, in asolve
    final_args, final_kwargs, call = cast_gen.send(kwargs)
                                     ^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/core/model.py", line 274, in _solve
    casted_model = self.model(**solved_kw)
                   ^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/pydantic/main.py", line 171, in __init__
    self.__pydantic_validator__.validate_python(data, self_instance=self)
pydantic_core._pydantic_core.ValidationError: 1 validation error for update_feed
feed_id
  Input should be a valid integer [type=int_type, input_value={'item': {'id': 78, 'titl...e': None}, 'feed_id': 1}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.6/v/int_type
2024-03-20 13:11:21,353 INFO     - product_feeds | product_feeds.one_feed_update_requested | 69ca5f80-3 - Processed
2024-03-20 13:11:21,353 ERROR    - product_feeds | product_feeds.one_feed_update_requested | 3f92e1ba-2 - ValidationError: 1 validation error for update_feed
feed_id
  Input should be a valid integer [type=int_type, input_value={'item': {'id': 76, 'titl...e': None}, 'feed_id': 1}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.6/v/int_type
Traceback (most recent call last):
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/handler.py", line 367, in consume
    raise e
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/handler.py", line 331, in consume
    result = await cast(
             ^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/utils.py", line 95, in set_message_wrapper
    return await func(message)
           ^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/nats/broker.py", line 244, in process_wrapper
    r = await func(message)
        ^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/core/asynchronous.py", line 406, in decode_wrapper
    return await func(msg)
           ^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/use.py", line 146, in injected_wrapper
    r = await real_model.asolve(
        ^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/core/model.py", line 519, in asolve
    final_args, final_kwargs, call = cast_gen.send(kwargs)
                                     ^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/core/model.py", line 274, in _solve
    casted_model = self.model(**solved_kw)
                   ^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/pydantic/main.py", line 171, in __init__
    self.__pydantic_validator__.validate_python(data, self_instance=self)
pydantic_core._pydantic_core.ValidationError: 1 validation error for update_feed
feed_id
  Input should be a valid integer [type=int_type, input_value={'item': {'id': 76, 'titl...e': None}, 'feed_id': 1}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.6/v/int_type
2024-03-20 13:11:21,361 INFO     - product_feeds | product_feeds.one_feed_update_requested | 3f92e1ba-2 - Processed
2024-03-20 13:11:21,363 INFO     - product_feeds | product_feeds.one_feed_update_requested | eaeaf43d-1 - Received
2024-03-20 13:11:21,363 INFO     - product_feeds | product_feeds.one_feed_update_requested | 218e3f33-6 - Received
2024-03-20 13:11:21,363 INFO     - product_feeds | product_feeds.one_feed_update_requested | 957660c3-4 - Received
2024-03-20 13:11:21,363 INFO     - product_feeds | product_feeds.one_feed_update_requested | 7d939aeb-5 - Received
2024-03-20 13:11:21,363 INFO     - product_feeds | product_feeds.one_feed_update_requested | 8f41a979-e - Received
2024-03-20 13:11:21,363 INFO     - product_feeds | product_feeds.one_feed_update_requested | 3e4f6db9-2 - Received
2024-03-20 13:11:21,363 INFO     - product_feeds | product_feeds.one_feed_update_requested | e3a36851-3 - Received
2024-03-20 13:11:21,363 INFO     - product_feeds | product_feeds.one_feed_update_requested | 9f3fef89-e - Received
2024-03-20 13:11:21,364 INFO     - product_feeds | product_feeds.one_feed_update_requested | d5beb0e6-6 - Received
2024-03-20 13:11:21,364 INFO     - product_feeds | product_feeds.one_feed_update_requested | d3041d69-e - Received
2024-03-20 13:11:21,365 ERROR    - product_feeds | product_feeds.one_feed_update_requested | 218e3f33-6 - ValidationError: 1 validation error for update_feed
feed_id
  Input should be a valid integer [type=int_type, input_value={'item': {'id': 87, 'titl...e': None}, 'feed_id': 1}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.6/v/int_type
Traceback (most recent call last):
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/handler.py", line 367, in consume
    raise e
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/handler.py", line 331, in consume
    result = await cast(
             ^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/utils.py", line 95, in set_message_wrapper
    return await func(message)
           ^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/nats/broker.py", line 244, in process_wrapper
    r = await func(message)
        ^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/core/asynchronous.py", line 406, in decode_wrapper
    return await func(msg)
           ^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/use.py", line 146, in injected_wrapper
    r = await real_model.asolve(
        ^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/core/model.py", line 519, in asolve
    final_args, final_kwargs, call = cast_gen.send(kwargs)
                                     ^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/core/model.py", line 274, in _solve
    casted_model = self.model(**solved_kw)
                   ^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/pydantic/main.py", line 171, in __init__
    self.__pydantic_validator__.validate_python(data, self_instance=self)
pydantic_core._pydantic_core.ValidationError: 1 validation error for update_feed
feed_id
  Input should be a valid integer [type=int_type, input_value={'item': {'id': 87, 'titl...e': None}, 'feed_id': 1}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.6/v/int_type
2024-03-20 13:11:21,366 INFO     - product_feeds | product_feeds.one_feed_update_requested | 218e3f33-6 - Processed
2024-03-20 13:11:21,366 ERROR    - product_feeds | product_feeds.one_feed_update_requested | 9f3fef89-e - ValidationError: 1 validation error for update_feed
feed_id
  Input should be a valid integer [type=int_type, input_value={'item': {'id': 93, 'titl...e': None}, 'feed_id': 1}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.6/v/int_type
Traceback (most recent call last):
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/handler.py", line 367, in consume
    raise e
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/handler.py", line 331, in consume
    result = await cast(
             ^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/utils.py", line 95, in set_message_wrapper
    return await func(message)
           ^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/nats/broker.py", line 244, in process_wrapper
    r = await func(message)
        ^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/core/asynchronous.py", line 406, in decode_wrapper
    return await func(msg)
           ^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/use.py", line 146, in injected_wrapper
    r = await real_model.asolve(
        ^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/core/model.py", line 519, in asolve
    final_args, final_kwargs, call = cast_gen.send(kwargs)
                                     ^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/core/model.py", line 274, in _solve
    casted_model = self.model(**solved_kw)
                   ^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/pydantic/main.py", line 171, in __init__
    self.__pydantic_validator__.validate_python(data, self_instance=self)
pydantic_core._pydantic_core.ValidationError: 1 validation error for update_feed
feed_id
  Input should be a valid integer [type=int_type, input_value={'item': {'id': 93, 'titl...e': None}, 'feed_id': 1}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.6/v/int_type
2024-03-20 13:11:21,367 INFO     - product_feeds | product_feeds.one_feed_update_requested | 9f3fef89-e - Processed
2024-03-20 13:11:21,367 ERROR    - product_feeds | product_feeds.one_feed_update_requested | 3e4f6db9-2 - ValidationError: 1 validation error for update_feed
feed_id
  Input should be a valid integer [type=int_type, input_value={'item': {'id': 91, 'titl...e': None}, 'feed_id': 1}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.6/v/int_type
Traceback (most recent call last):
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/handler.py", line 367, in consume
    raise e
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/handler.py", line 331, in consume
    result = await cast(
             ^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/utils.py", line 95, in set_message_wrapper
    return await func(message)
           ^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/nats/broker.py", line 244, in process_wrapper
    r = await func(message)
        ^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/core/asynchronous.py", line 406, in decode_wrapper
    return await func(msg)
           ^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/use.py", line 146, in injected_wrapper
    r = await real_model.asolve(
        ^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/core/model.py", line 519, in asolve
    final_args, final_kwargs, call = cast_gen.send(kwargs)
                                     ^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/core/model.py", line 274, in _solve
    casted_model = self.model(**solved_kw)
                   ^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/pydantic/main.py", line 171, in __init__
    self.__pydantic_validator__.validate_python(data, self_instance=self)
pydantic_core._pydantic_core.ValidationError: 1 validation error for update_feed
feed_id
  Input should be a valid integer [type=int_type, input_value={'item': {'id': 91, 'titl...e': None}, 'feed_id': 1}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.6/v/int_type
2024-03-20 13:11:21,368 INFO     - product_feeds | product_feeds.one_feed_update_requested | 3e4f6db9-2 - Processed
2024-03-20 13:11:21,368 ERROR    - product_feeds | product_feeds.one_feed_update_requested | 7d939aeb-5 - ValidationError: 1 validation error for update_feed
feed_id
  Input should be a valid integer [type=int_type, input_value={'item': {'id': 89, 'titl...e': None}, 'feed_id': 1}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.6/v/int_type
Traceback (most recent call last):
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/handler.py", line 367, in consume
    raise e
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/handler.py", line 331, in consume
    result = await cast(
             ^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/utils.py", line 95, in set_message_wrapper
    return await func(message)
           ^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/nats/broker.py", line 244, in process_wrapper
    r = await func(message)
        ^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/core/asynchronous.py", line 406, in decode_wrapper
    return await func(msg)
           ^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/use.py", line 146, in injected_wrapper
    r = await real_model.asolve(
        ^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/core/model.py", line 519, in asolve
    final_args, final_kwargs, call = cast_gen.send(kwargs)
                                     ^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/core/model.py", line 274, in _solve
    casted_model = self.model(**solved_kw)
                   ^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/pydantic/main.py", line 171, in __init__
    self.__pydantic_validator__.validate_python(data, self_instance=self)
pydantic_core._pydantic_core.ValidationError: 1 validation error for update_feed
feed_id
  Input should be a valid integer [type=int_type, input_value={'item': {'id': 89, 'titl...e': None}, 'feed_id': 1}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.6/v/int_type
2024-03-20 13:11:21,369 INFO     - product_feeds | product_feeds.one_feed_update_requested | 7d939aeb-5 - Processed
2024-03-20 13:11:21,369 ERROR    - product_feeds | product_feeds.one_feed_update_requested | e3a36851-3 - ValidationError: 1 validation error for update_feed
feed_id
  Input should be a valid integer [type=int_type, input_value={'item': {'id': 92, 'titl...e': None}, 'feed_id': 1}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.6/v/int_type
Traceback (most recent call last):
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/handler.py", line 367, in consume
    raise e
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/handler.py", line 331, in consume
    result = await cast(
             ^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/utils.py", line 95, in set_message_wrapper
    return await func(message)
           ^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/nats/broker.py", line 244, in process_wrapper
    r = await func(message)
        ^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/core/asynchronous.py", line 406, in decode_wrapper
    return await func(msg)
           ^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/use.py", line 146, in injected_wrapper
    r = await real_model.asolve(
        ^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/core/model.py", line 519, in asolve
    final_args, final_kwargs, call = cast_gen.send(kwargs)
                                     ^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/core/model.py", line 274, in _solve
    casted_model = self.model(**solved_kw)
                   ^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/pydantic/main.py", line 171, in __init__
    self.__pydantic_validator__.validate_python(data, self_instance=self)
pydantic_core._pydantic_core.ValidationError: 1 validation error for update_feed
feed_id
  Input should be a valid integer [type=int_type, input_value={'item': {'id': 92, 'titl...e': None}, 'feed_id': 1}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.6/v/int_type
2024-03-20 13:11:21,370 INFO     - product_feeds | product_feeds.one_feed_update_requested | e3a36851-3 - Processed
2024-03-20 13:11:21,370 ERROR    - product_feeds | product_feeds.one_feed_update_requested | eaeaf43d-1 - ValidationError: 1 validation error for update_feed
feed_id
  Input should be a valid integer [type=int_type, input_value={'item': {'id': 86, 'titl...e': None}, 'feed_id': 1}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.6/v/int_type
Traceback (most recent call last):
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/handler.py", line 367, in consume
    raise e
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/handler.py", line 331, in consume
    result = await cast(
             ^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/utils.py", line 95, in set_message_wrapper
    return await func(message)
           ^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/nats/broker.py", line 244, in process_wrapper
    r = await func(message)
        ^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/core/asynchronous.py", line 406, in decode_wrapper
    return await func(msg)
           ^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/use.py", line 146, in injected_wrapper
    r = await real_model.asolve(
        ^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/core/model.py", line 519, in asolve
    final_args, final_kwargs, call = cast_gen.send(kwargs)
                                     ^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/core/model.py", line 274, in _solve
    casted_model = self.model(**solved_kw)
                   ^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/pydantic/main.py", line 171, in __init__
    self.__pydantic_validator__.validate_python(data, self_instance=self)
pydantic_core._pydantic_core.ValidationError: 1 validation error for update_feed
feed_id
  Input should be a valid integer [type=int_type, input_value={'item': {'id': 86, 'titl...e': None}, 'feed_id': 1}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.6/v/int_type
2024-03-20 13:11:21,371 INFO     - product_feeds | product_feeds.one_feed_update_requested | eaeaf43d-1 - Processed
2024-03-20 13:11:21,371 ERROR    - product_feeds | product_feeds.one_feed_update_requested | d5beb0e6-6 - ValidationError: 1 validation error for update_feed
feed_id
  Input should be a valid integer [type=int_type, input_value={'item': {'id': 94, 'titl...e': None}, 'feed_id': 1}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.6/v/int_type
Traceback (most recent call last):
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/handler.py", line 367, in consume
    raise e
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/handler.py", line 331, in consume
    result = await cast(
             ^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/utils.py", line 95, in set_message_wrapper
    return await func(message)
           ^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/nats/broker.py", line 244, in process_wrapper
    r = await func(message)
        ^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/core/asynchronous.py", line 406, in decode_wrapper
    return await func(msg)
           ^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/use.py", line 146, in injected_wrapper
    r = await real_model.asolve(
        ^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/core/model.py", line 519, in asolve
    final_args, final_kwargs, call = cast_gen.send(kwargs)
                                     ^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/core/model.py", line 274, in _solve
    casted_model = self.model(**solved_kw)
                   ^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/pydantic/main.py", line 171, in __init__
    self.__pydantic_validator__.validate_python(data, self_instance=self)
pydantic_core._pydantic_core.ValidationError: 1 validation error for update_feed
feed_id
  Input should be a valid integer [type=int_type, input_value={'item': {'id': 94, 'titl...e': None}, 'feed_id': 1}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.6/v/int_type
2024-03-20 13:11:21,372 INFO     - product_feeds | product_feeds.one_feed_update_requested | d5beb0e6-6 - Processed
2024-03-20 13:11:21,372 ERROR    - product_feeds | product_feeds.one_feed_update_requested | 8f41a979-e - ValidationError: 1 validation error for update_feed
feed_id
  Input should be a valid integer [type=int_type, input_value={'item': {'id': 90, 'titl...e': None}, 'feed_id': 1}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.6/v/int_type
Traceback (most recent call last):
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/handler.py", line 367, in consume
    raise e
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/handler.py", line 331, in consume
    result = await cast(
             ^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/utils.py", line 95, in set_message_wrapper
    return await func(message)
           ^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/nats/broker.py", line 244, in process_wrapper
    r = await func(message)
        ^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/core/asynchronous.py", line 406, in decode_wrapper
    return await func(msg)
           ^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/use.py", line 146, in injected_wrapper
    r = await real_model.asolve(
        ^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/core/model.py", line 519, in asolve
    final_args, final_kwargs, call = cast_gen.send(kwargs)
                                     ^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/core/model.py", line 274, in _solve
    casted_model = self.model(**solved_kw)
                   ^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/pydantic/main.py", line 171, in __init__
    self.__pydantic_validator__.validate_python(data, self_instance=self)
pydantic_core._pydantic_core.ValidationError: 1 validation error for update_feed
feed_id
  Input should be a valid integer [type=int_type, input_value={'item': {'id': 90, 'titl...e': None}, 'feed_id': 1}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.6/v/int_type
2024-03-20 13:11:21,373 INFO     - product_feeds | product_feeds.one_feed_update_requested | 8f41a979-e - Processed
2024-03-20 13:11:21,373 ERROR    - product_feeds | product_feeds.one_feed_update_requested | d3041d69-e - ValidationError: 1 validation error for update_feed
feed_id
  Input should be a valid integer [type=int_type, input_value={'item': {'id': 95, 'titl...e': None}, 'feed_id': 1}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.6/v/int_type
Traceback (most recent call last):
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/handler.py", line 367, in consume
    raise e
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/handler.py", line 331, in consume
    result = await cast(
             ^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/utils.py", line 95, in set_message_wrapper
    return await func(message)
           ^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/nats/broker.py", line 244, in process_wrapper
    r = await func(message)
        ^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/core/asynchronous.py", line 406, in decode_wrapper
    return await func(msg)
           ^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/use.py", line 146, in injected_wrapper
    r = await real_model.asolve(
        ^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/core/model.py", line 519, in asolve
    final_args, final_kwargs, call = cast_gen.send(kwargs)
                                     ^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/core/model.py", line 274, in _solve
    casted_model = self.model(**solved_kw)
                   ^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/pydantic/main.py", line 171, in __init__
    self.__pydantic_validator__.validate_python(data, self_instance=self)
pydantic_core._pydantic_core.ValidationError: 1 validation error for update_feed
feed_id
  Input should be a valid integer [type=int_type, input_value={'item': {'id': 95, 'titl...e': None}, 'feed_id': 1}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.6/v/int_type
2024-03-20 13:11:21,374 INFO     - product_feeds | product_feeds.one_feed_update_requested | d3041d69-e - Processed
2024-03-20 13:11:21,374 ERROR    - product_feeds | product_feeds.one_feed_update_requested | 957660c3-4 - ValidationError: 1 validation error for update_feed
feed_id
  Input should be a valid integer [type=int_type, input_value={'item': {'id': 88, 'titl...e': None}, 'feed_id': 1}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.6/v/int_type
Traceback (most recent call last):
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/handler.py", line 367, in consume
    raise e
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/handler.py", line 331, in consume
    result = await cast(
             ^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/utils.py", line 95, in set_message_wrapper
    return await func(message)
           ^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/nats/broker.py", line 244, in process_wrapper
    r = await func(message)
        ^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/core/asynchronous.py", line 406, in decode_wrapper
    return await func(msg)
           ^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/use.py", line 146, in injected_wrapper
    r = await real_model.asolve(
        ^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/core/model.py", line 519, in asolve
    final_args, final_kwargs, call = cast_gen.send(kwargs)
                                     ^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/core/model.py", line 274, in _solve
    casted_model = self.model(**solved_kw)
                   ^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/pydantic/main.py", line 171, in __init__
    self.__pydantic_validator__.validate_python(data, self_instance=self)
pydantic_core._pydantic_core.ValidationError: 1 validation error for update_feed
feed_id
  Input should be a valid integer [type=int_type, input_value={'item': {'id': 88, 'titl...e': None}, 'feed_id': 1}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.6/v/int_type
2024-03-20 13:11:21,381 INFO     - product_feeds | product_feeds.one_feed_update_requested | 957660c3-4 - Processed
2024-03-20 13:11:21,384 INFO     - product_feeds | product_feeds.one_feed_update_requested | 427c71c1-8 - Received
2024-03-20 13:11:21,384 INFO     - product_feeds | product_feeds.one_feed_update_requested | 744010cd-e - Received
2024-03-20 13:11:21,384 INFO     - product_feeds | product_feeds.one_feed_update_requested | 0896f6b8-1 - Received
2024-03-20 13:11:21,384 INFO     - product_feeds | product_feeds.one_feed_update_requested | 4b1d14ae-0 - Received
2024-03-20 13:11:21,384 INFO     - product_feeds | product_feeds.one_feed_update_requested | f18428a9-9 - Received
2024-03-20 13:11:21,384 INFO     - product_feeds | product_feeds.one_feed_update_requested | bdf02ed3-2 - Received
2024-03-20 13:11:21,384 INFO     - product_feeds | product_feeds.one_feed_update_requested | cdf334de-3 - Received
2024-03-20 13:11:21,384 INFO     - product_feeds | product_feeds.one_feed_update_requested | 795f8b54-3 - Received
2024-03-20 13:11:21,384 INFO     - product_feeds | product_feeds.one_feed_update_requested | e53dfc2f-2 - Received
2024-03-20 13:11:21,385 INFO     - product_feeds | product_feeds.one_feed_update_requested | 217a8b0e-6 - Received
2024-03-20 13:11:21,387 ERROR    - product_feeds | product_feeds.one_feed_update_requested | f18428a9-9 - ValidationError: 1 validation error for update_feed
feed_id
  Input should be a valid integer [type=int_type, input_value={'item': {'id': 100, 'tit...e': None}, 'feed_id': 1}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.6/v/int_type
Traceback (most recent call last):
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/handler.py", line 367, in consume
    raise e
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/handler.py", line 331, in consume
    result = await cast(
             ^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/utils.py", line 95, in set_message_wrapper
    return await func(message)
           ^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/nats/broker.py", line 244, in process_wrapper
    r = await func(message)
        ^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/core/asynchronous.py", line 406, in decode_wrapper
    return await func(msg)
           ^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/use.py", line 146, in injected_wrapper
    r = await real_model.asolve(
        ^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/core/model.py", line 519, in asolve
    final_args, final_kwargs, call = cast_gen.send(kwargs)
                                     ^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/core/model.py", line 274, in _solve
    casted_model = self.model(**solved_kw)
                   ^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/pydantic/main.py", line 171, in __init__
    self.__pydantic_validator__.validate_python(data, self_instance=self)
pydantic_core._pydantic_core.ValidationError: 1 validation error for update_feed
feed_id
  Input should be a valid integer [type=int_type, input_value={'item': {'id': 100, 'tit...e': None}, 'feed_id': 1}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.6/v/int_type
2024-03-20 13:11:21,388 INFO     - product_feeds | product_feeds.one_feed_update_requested | f18428a9-9 - Processed
2024-03-20 13:11:21,388 ERROR    - product_feeds | product_feeds.one_feed_update_requested | 0896f6b8-1 - ValidationError: 1 validation error for update_feed
feed_id
  Input should be a valid integer [type=int_type, input_value={'item': {'id': 98, 'titl...e': None}, 'feed_id': 1}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.6/v/int_type
Traceback (most recent call last):
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/handler.py", line 367, in consume
    raise e
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/handler.py", line 331, in consume
    result = await cast(
             ^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/utils.py", line 95, in set_message_wrapper
    return await func(message)
           ^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/nats/broker.py", line 244, in process_wrapper
    r = await func(message)
        ^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/core/asynchronous.py", line 406, in decode_wrapper
    return await func(msg)
           ^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/use.py", line 146, in injected_wrapper
    r = await real_model.asolve(
        ^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/core/model.py", line 519, in asolve
    final_args, final_kwargs, call = cast_gen.send(kwargs)
                                     ^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/core/model.py", line 274, in _solve
    casted_model = self.model(**solved_kw)
                   ^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/pydantic/main.py", line 171, in __init__
    self.__pydantic_validator__.validate_python(data, self_instance=self)
pydantic_core._pydantic_core.ValidationError: 1 validation error for update_feed
feed_id
  Input should be a valid integer [type=int_type, input_value={'item': {'id': 98, 'titl...e': None}, 'feed_id': 1}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.6/v/int_type
2024-03-20 13:11:21,389 INFO     - product_feeds | product_feeds.one_feed_update_requested | 0896f6b8-1 - Processed
2024-03-20 13:11:21,389 ERROR    - product_feeds | product_feeds.one_feed_update_requested | bdf02ed3-2 - ValidationError: 1 validation error for update_feed
feed_id
  Input should be a valid integer [type=int_type, input_value={'item': {'id': 101, 'tit...e': None}, 'feed_id': 1}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.6/v/int_type
Traceback (most recent call last):
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/handler.py", line 367, in consume
    raise e
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/handler.py", line 331, in consume
    result = await cast(
             ^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/utils.py", line 95, in set_message_wrapper
    return await func(message)
           ^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/nats/broker.py", line 244, in process_wrapper
    r = await func(message)
        ^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/core/asynchronous.py", line 406, in decode_wrapper
    return await func(msg)
           ^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/use.py", line 146, in injected_wrapper
    r = await real_model.asolve(
        ^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/core/model.py", line 519, in asolve
    final_args, final_kwargs, call = cast_gen.send(kwargs)
                                     ^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/core/model.py", line 274, in _solve
    casted_model = self.model(**solved_kw)
                   ^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/pydantic/main.py", line 171, in __init__
    self.__pydantic_validator__.validate_python(data, self_instance=self)
pydantic_core._pydantic_core.ValidationError: 1 validation error for update_feed
feed_id
  Input should be a valid integer [type=int_type, input_value={'item': {'id': 101, 'tit...e': None}, 'feed_id': 1}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.6/v/int_type
2024-03-20 13:11:21,390 INFO     - product_feeds | product_feeds.one_feed_update_requested | bdf02ed3-2 - Processed
2024-03-20 13:11:21,390 ERROR    - product_feeds | product_feeds.one_feed_update_requested | e53dfc2f-2 - ValidationError: 1 validation error for update_feed
feed_id
  Input should be a valid integer [type=int_type, input_value={'item': {'id': 104, 'tit...e': None}, 'feed_id': 1}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.6/v/int_type
Traceback (most recent call last):
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/handler.py", line 367, in consume
    raise e
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/handler.py", line 331, in consume
    result = await cast(
             ^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/utils.py", line 95, in set_message_wrapper
    return await func(message)
           ^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/nats/broker.py", line 244, in process_wrapper
    r = await func(message)
        ^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/core/asynchronous.py", line 406, in decode_wrapper
    return await func(msg)
           ^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/use.py", line 146, in injected_wrapper
    r = await real_model.asolve(
        ^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/core/model.py", line 519, in asolve
    final_args, final_kwargs, call = cast_gen.send(kwargs)
                                     ^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/core/model.py", line 274, in _solve
    casted_model = self.model(**solved_kw)
                   ^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/pydantic/main.py", line 171, in __init__
    self.__pydantic_validator__.validate_python(data, self_instance=self)
pydantic_core._pydantic_core.ValidationError: 1 validation error for update_feed
feed_id
  Input should be a valid integer [type=int_type, input_value={'item': {'id': 104, 'tit...e': None}, 'feed_id': 1}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.6/v/int_type
2024-03-20 13:11:21,391 INFO     - product_feeds | product_feeds.one_feed_update_requested | e53dfc2f-2 - Processed
2024-03-20 13:11:21,391 ERROR    - product_feeds | product_feeds.one_feed_update_requested | 217a8b0e-6 - ValidationError: 1 validation error for update_feed
feed_id
  Input should be a valid integer [type=int_type, input_value={'item': {'id': 105, 'tit...e': None}, 'feed_id': 1}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.6/v/int_type
Traceback (most recent call last):
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/handler.py", line 367, in consume
    raise e
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/handler.py", line 331, in consume
    result = await cast(
             ^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/utils.py", line 95, in set_message_wrapper
    return await func(message)
           ^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/nats/broker.py", line 244, in process_wrapper
    r = await func(message)
        ^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/core/asynchronous.py", line 406, in decode_wrapper
    return await func(msg)
           ^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/use.py", line 146, in injected_wrapper
    r = await real_model.asolve(
        ^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/core/model.py", line 519, in asolve
    final_args, final_kwargs, call = cast_gen.send(kwargs)
                                     ^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/core/model.py", line 274, in _solve
    casted_model = self.model(**solved_kw)
                   ^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/pydantic/main.py", line 171, in __init__
    self.__pydantic_validator__.validate_python(data, self_instance=self)
pydantic_core._pydantic_core.ValidationError: 1 validation error for update_feed
feed_id
  Input should be a valid integer [type=int_type, input_value={'item': {'id': 105, 'tit...e': None}, 'feed_id': 1}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.6/v/int_type
2024-03-20 13:11:21,392 INFO     - product_feeds | product_feeds.one_feed_update_requested | 217a8b0e-6 - Processed
2024-03-20 13:11:21,392 ERROR    - product_feeds | product_feeds.one_feed_update_requested | 744010cd-e - ValidationError: 1 validation error for update_feed
feed_id
  Input should be a valid integer [type=int_type, input_value={'item': {'id': 97, 'titl...e': None}, 'feed_id': 1}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.6/v/int_type
Traceback (most recent call last):
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/handler.py", line 367, in consume
    raise e
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/handler.py", line 331, in consume
    result = await cast(
             ^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/utils.py", line 95, in set_message_wrapper
    return await func(message)
           ^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/nats/broker.py", line 244, in process_wrapper
    r = await func(message)
        ^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/core/asynchronous.py", line 406, in decode_wrapper
    return await func(msg)
           ^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/use.py", line 146, in injected_wrapper
    r = await real_model.asolve(
        ^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/core/model.py", line 519, in asolve
    final_args, final_kwargs, call = cast_gen.send(kwargs)
                                     ^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/core/model.py", line 274, in _solve
    casted_model = self.model(**solved_kw)
                   ^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/pydantic/main.py", line 171, in __init__
    self.__pydantic_validator__.validate_python(data, self_instance=self)
pydantic_core._pydantic_core.ValidationError: 1 validation error for update_feed
feed_id
  Input should be a valid integer [type=int_type, input_value={'item': {'id': 97, 'titl...e': None}, 'feed_id': 1}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.6/v/int_type
2024-03-20 13:11:21,393 INFO     - product_feeds | product_feeds.one_feed_update_requested | 744010cd-e - Processed
2024-03-20 13:11:21,393 ERROR    - product_feeds | product_feeds.one_feed_update_requested | 795f8b54-3 - ValidationError: 1 validation error for update_feed
feed_id
  Input should be a valid integer [type=int_type, input_value={'item': {'id': 103, 'tit...e': None}, 'feed_id': 1}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.6/v/int_type
Traceback (most recent call last):
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/handler.py", line 367, in consume
    raise e
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/handler.py", line 331, in consume
    result = await cast(
             ^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/utils.py", line 95, in set_message_wrapper
    return await func(message)
           ^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/nats/broker.py", line 244, in process_wrapper
    r = await func(message)
        ^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/core/asynchronous.py", line 406, in decode_wrapper
    return await func(msg)
           ^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/use.py", line 146, in injected_wrapper
    r = await real_model.asolve(
        ^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/core/model.py", line 519, in asolve
    final_args, final_kwargs, call = cast_gen.send(kwargs)
                                     ^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/core/model.py", line 274, in _solve
    casted_model = self.model(**solved_kw)
                   ^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/pydantic/main.py", line 171, in __init__
    self.__pydantic_validator__.validate_python(data, self_instance=self)
pydantic_core._pydantic_core.ValidationError: 1 validation error for update_feed
feed_id
  Input should be a valid integer [type=int_type, input_value={'item': {'id': 103, 'tit...e': None}, 'feed_id': 1}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.6/v/int_type
2024-03-20 13:11:21,394 INFO     - product_feeds | product_feeds.one_feed_update_requested | 795f8b54-3 - Processed
2024-03-20 13:11:21,394 ERROR    - product_feeds | product_feeds.one_feed_update_requested | 427c71c1-8 - ValidationError: 1 validation error for update_feed
feed_id
  Input should be a valid integer [type=int_type, input_value={'item': {'id': 96, 'titl...e': None}, 'feed_id': 1}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.6/v/int_type
Traceback (most recent call last):
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/handler.py", line 367, in consume
    raise e
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/handler.py", line 331, in consume
    result = await cast(
             ^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/utils.py", line 95, in set_message_wrapper
    return await func(message)
           ^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/nats/broker.py", line 244, in process_wrapper
    r = await func(message)
        ^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/core/asynchronous.py", line 406, in decode_wrapper
    return await func(msg)
           ^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/use.py", line 146, in injected_wrapper
    r = await real_model.asolve(
        ^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/core/model.py", line 519, in asolve
    final_args, final_kwargs, call = cast_gen.send(kwargs)
                                     ^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/core/model.py", line 274, in _solve
    casted_model = self.model(**solved_kw)
                   ^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/pydantic/main.py", line 171, in __init__
    self.__pydantic_validator__.validate_python(data, self_instance=self)
pydantic_core._pydantic_core.ValidationError: 1 validation error for update_feed
feed_id
  Input should be a valid integer [type=int_type, input_value={'item': {'id': 96, 'titl...e': None}, 'feed_id': 1}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.6/v/int_type
2024-03-20 13:11:21,395 INFO     - product_feeds | product_feeds.one_feed_update_requested | 427c71c1-8 - Processed
2024-03-20 13:11:21,395 ERROR    - product_feeds | product_feeds.one_feed_update_requested | 4b1d14ae-0 - ValidationError: 1 validation error for update_feed
feed_id
  Input should be a valid integer [type=int_type, input_value={'item': {'id': 99, 'titl...e': None}, 'feed_id': 1}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.6/v/int_type
Traceback (most recent call last):
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/handler.py", line 367, in consume
    raise e
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/handler.py", line 331, in consume
    result = await cast(
             ^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/utils.py", line 95, in set_message_wrapper
    return await func(message)
           ^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/nats/broker.py", line 244, in process_wrapper
    r = await func(message)
        ^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/core/asynchronous.py", line 406, in decode_wrapper
    return await func(msg)
           ^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/use.py", line 146, in injected_wrapper
    r = await real_model.asolve(
        ^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/core/model.py", line 519, in asolve
    final_args, final_kwargs, call = cast_gen.send(kwargs)
                                     ^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/core/model.py", line 274, in _solve
    casted_model = self.model(**solved_kw)
                   ^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/pydantic/main.py", line 171, in __init__
    self.__pydantic_validator__.validate_python(data, self_instance=self)
pydantic_core._pydantic_core.ValidationError: 1 validation error for update_feed
feed_id
  Input should be a valid integer [type=int_type, input_value={'item': {'id': 99, 'titl...e': None}, 'feed_id': 1}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.6/v/int_type
2024-03-20 13:11:21,396 INFO     - product_feeds | product_feeds.one_feed_update_requested | 4b1d14ae-0 - Processed
2024-03-20 13:11:21,396 ERROR    - product_feeds | product_feeds.one_feed_update_requested | cdf334de-3 - ValidationError: 1 validation error for update_feed
feed_id
  Input should be a valid integer [type=int_type, input_value={'item': {'id': 102, 'tit...e': None}, 'feed_id': 1}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.6/v/int_type
Traceback (most recent call last):
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/handler.py", line 367, in consume
    raise e
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/handler.py", line 331, in consume
    result = await cast(
             ^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/utils.py", line 95, in set_message_wrapper
    return await func(message)
           ^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/nats/broker.py", line 244, in process_wrapper
    r = await func(message)
        ^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/core/asynchronous.py", line 406, in decode_wrapper
    return await func(msg)
           ^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/use.py", line 146, in injected_wrapper
    r = await real_model.asolve(
        ^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/core/model.py", line 519, in asolve
    final_args, final_kwargs, call = cast_gen.send(kwargs)
                                     ^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/core/model.py", line 274, in _solve
    casted_model = self.model(**solved_kw)
                   ^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/pydantic/main.py", line 171, in __init__
    self.__pydantic_validator__.validate_python(data, self_instance=self)
pydantic_core._pydantic_core.ValidationError: 1 validation error for update_feed
feed_id
  Input should be a valid integer [type=int_type, input_value={'item': {'id': 102, 'tit...e': None}, 'feed_id': 1}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.6/v/int_type
2024-03-20 13:11:21,403 INFO     - product_feeds | product_feeds.one_feed_update_requested | cdf334de-3 - Processed
2024-03-20 13:11:21,405 INFO     - product_feeds | product_feeds.one_feed_update_requested | f38438c1-8 - Received
2024-03-20 13:11:21,405 INFO     - product_feeds | product_feeds.one_feed_update_requested | ac1e37a9-2 - Received
2024-03-20 13:11:21,405 INFO     - product_feeds | product_feeds.one_feed_update_requested | 5fdd1705-8 - Received
2024-03-20 13:11:21,405 INFO     - product_feeds | product_feeds.one_feed_update_requested | 6f977e0c-b - Received
2024-03-20 13:11:21,405 INFO     - product_feeds | product_feeds.one_feed_update_requested | 35aed9db-d - Received
2024-03-20 13:11:21,405 INFO     - product_feeds | product_feeds.one_feed_update_requested | 0e987640-a - Received
2024-03-20 13:11:21,406 INFO     - product_feeds | product_feeds.one_feed_update_requested | 929a5770-3 - Received
2024-03-20 13:11:21,406 INFO     - product_feeds | product_feeds.one_feed_update_requested | cec664ab-8 - Received
2024-03-20 13:11:21,406 INFO     - product_feeds | product_feeds.one_feed_update_requested | dfc4ee48-e - Received
2024-03-20 13:11:21,406 INFO     - product_feeds | product_feeds.one_feed_update_requested | ba365302-f - Received
2024-03-20 13:11:21,407 ERROR    - product_feeds | product_feeds.one_feed_update_requested | 0e987640-a - ValidationError: 1 validation error for update_feed
feed_id
  Input should be a valid integer [type=int_type, input_value={'item': {'id': 111, 'tit...e': None}, 'feed_id': 1}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.6/v/int_type
Traceback (most recent call last):
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/handler.py", line 367, in consume
    raise e
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/handler.py", line 331, in consume
    result = await cast(
             ^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/utils.py", line 95, in set_message_wrapper
    return await func(message)
           ^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/nats/broker.py", line 244, in process_wrapper
    r = await func(message)
        ^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/core/asynchronous.py", line 406, in decode_wrapper
    return await func(msg)
           ^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/use.py", line 146, in injected_wrapper
    r = await real_model.asolve(
        ^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/core/model.py", line 519, in asolve
    final_args, final_kwargs, call = cast_gen.send(kwargs)
                                     ^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/core/model.py", line 274, in _solve
    casted_model = self.model(**solved_kw)
                   ^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/pydantic/main.py", line 171, in __init__
    self.__pydantic_validator__.validate_python(data, self_instance=self)
pydantic_core._pydantic_core.ValidationError: 1 validation error for update_feed
feed_id
  Input should be a valid integer [type=int_type, input_value={'item': {'id': 111, 'tit...e': None}, 'feed_id': 1}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.6/v/int_type
2024-03-20 13:11:21,408 INFO     - product_feeds | product_feeds.one_feed_update_requested | 0e987640-a - Processed
2024-03-20 13:11:21,409 ERROR    - product_feeds | product_feeds.one_feed_update_requested | f38438c1-8 - ValidationError: 1 validation error for update_feed
feed_id
  Input should be a valid integer [type=int_type, input_value={'item': {'id': 106, 'tit...e': None}, 'feed_id': 1}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.6/v/int_type
Traceback (most recent call last):
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/handler.py", line 367, in consume
    raise e
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/handler.py", line 331, in consume
    result = await cast(
             ^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/utils.py", line 95, in set_message_wrapper
    return await func(message)
           ^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/nats/broker.py", line 244, in process_wrapper
    r = await func(message)
        ^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/core/asynchronous.py", line 406, in decode_wrapper
    return await func(msg)
           ^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/use.py", line 146, in injected_wrapper
    r = await real_model.asolve(
        ^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/core/model.py", line 519, in asolve
    final_args, final_kwargs, call = cast_gen.send(kwargs)
                                     ^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/core/model.py", line 274, in _solve
    casted_model = self.model(**solved_kw)
                   ^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/pydantic/main.py", line 171, in __init__
    self.__pydantic_validator__.validate_python(data, self_instance=self)
pydantic_core._pydantic_core.ValidationError: 1 validation error for update_feed
feed_id
  Input should be a valid integer [type=int_type, input_value={'item': {'id': 106, 'tit...e': None}, 'feed_id': 1}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.6/v/int_type
2024-03-20 13:11:21,409 INFO     - product_feeds | product_feeds.one_feed_update_requested | f38438c1-8 - Processed
2024-03-20 13:11:21,410 ERROR    - product_feeds | product_feeds.one_feed_update_requested | 929a5770-3 - ValidationError: 1 validation error for update_feed
feed_id
  Input should be a valid integer [type=int_type, input_value={'item': {'id': 112, 'tit...e': None}, 'feed_id': 1}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.6/v/int_type
Traceback (most recent call last):
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/handler.py", line 367, in consume
    raise e
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/handler.py", line 331, in consume
    result = await cast(
             ^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/utils.py", line 95, in set_message_wrapper
    return await func(message)
           ^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/nats/broker.py", line 244, in process_wrapper
    r = await func(message)
        ^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/core/asynchronous.py", line 406, in decode_wrapper
    return await func(msg)
           ^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/use.py", line 146, in injected_wrapper
    r = await real_model.asolve(
        ^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/core/model.py", line 519, in asolve
    final_args, final_kwargs, call = cast_gen.send(kwargs)
                                     ^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/core/model.py", line 274, in _solve
    casted_model = self.model(**solved_kw)
                   ^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/pydantic/main.py", line 171, in __init__
    self.__pydantic_validator__.validate_python(data, self_instance=self)
pydantic_core._pydantic_core.ValidationError: 1 validation error for update_feed
feed_id
  Input should be a valid integer [type=int_type, input_value={'item': {'id': 112, 'tit...e': None}, 'feed_id': 1}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.6/v/int_type
2024-03-20 13:11:21,410 INFO     - product_feeds | product_feeds.one_feed_update_requested | 929a5770-3 - Processed
2024-03-20 13:11:21,410 ERROR    - product_feeds | product_feeds.one_feed_update_requested | cec664ab-8 - ValidationError: 1 validation error for update_feed
feed_id
  Input should be a valid integer [type=int_type, input_value={'item': {'id': 113, 'tit...e': None}, 'feed_id': 1}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.6/v/int_type
Traceback (most recent call last):
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/handler.py", line 367, in consume
    raise e
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/handler.py", line 331, in consume
    result = await cast(
             ^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/utils.py", line 95, in set_message_wrapper
    return await func(message)
           ^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/nats/broker.py", line 244, in process_wrapper
    r = await func(message)
        ^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/core/asynchronous.py", line 406, in decode_wrapper
    return await func(msg)
           ^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/use.py", line 146, in injected_wrapper
    r = await real_model.asolve(
        ^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/core/model.py", line 519, in asolve
    final_args, final_kwargs, call = cast_gen.send(kwargs)
                                     ^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/core/model.py", line 274, in _solve
    casted_model = self.model(**solved_kw)
                   ^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/pydantic/main.py", line 171, in __init__
    self.__pydantic_validator__.validate_python(data, self_instance=self)
pydantic_core._pydantic_core.ValidationError: 1 validation error for update_feed
feed_id
  Input should be a valid integer [type=int_type, input_value={'item': {'id': 113, 'tit...e': None}, 'feed_id': 1}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.6/v/int_type
2024-03-20 13:11:21,411 INFO     - product_feeds | product_feeds.one_feed_update_requested | cec664ab-8 - Processed
2024-03-20 13:11:21,411 ERROR    - product_feeds | product_feeds.one_feed_update_requested | 6f977e0c-b - ValidationError: 1 validation error for update_feed
feed_id
  Input should be a valid integer [type=int_type, input_value={'item': {'id': 109, 'tit...e': None}, 'feed_id': 1}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.6/v/int_type
Traceback (most recent call last):
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/handler.py", line 367, in consume
    raise e
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/handler.py", line 331, in consume
    result = await cast(
             ^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/utils.py", line 95, in set_message_wrapper
    return await func(message)
           ^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/nats/broker.py", line 244, in process_wrapper
    r = await func(message)
        ^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/core/asynchronous.py", line 406, in decode_wrapper
    return await func(msg)
           ^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/use.py", line 146, in injected_wrapper
    r = await real_model.asolve(
        ^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/core/model.py", line 519, in asolve
    final_args, final_kwargs, call = cast_gen.send(kwargs)
                                     ^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/core/model.py", line 274, in _solve
    casted_model = self.model(**solved_kw)
                   ^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/pydantic/main.py", line 171, in __init__
    self.__pydantic_validator__.validate_python(data, self_instance=self)
pydantic_core._pydantic_core.ValidationError: 1 validation error for update_feed
feed_id
  Input should be a valid integer [type=int_type, input_value={'item': {'id': 109, 'tit...e': None}, 'feed_id': 1}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.6/v/int_type
2024-03-20 13:11:21,412 INFO     - product_feeds | product_feeds.one_feed_update_requested | 6f977e0c-b - Processed
2024-03-20 13:11:21,412 ERROR    - product_feeds | product_feeds.one_feed_update_requested | 35aed9db-d - ValidationError: 1 validation error for update_feed
feed_id
  Input should be a valid integer [type=int_type, input_value={'item': {'id': 110, 'tit...e': None}, 'feed_id': 1}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.6/v/int_type
Traceback (most recent call last):
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/handler.py", line 367, in consume
    raise e
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/handler.py", line 331, in consume
    result = await cast(
             ^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/utils.py", line 95, in set_message_wrapper
    return await func(message)
           ^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/nats/broker.py", line 244, in process_wrapper
    r = await func(message)
        ^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/core/asynchronous.py", line 406, in decode_wrapper
    return await func(msg)
           ^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/use.py", line 146, in injected_wrapper
    r = await real_model.asolve(
        ^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/core/model.py", line 519, in asolve
    final_args, final_kwargs, call = cast_gen.send(kwargs)
                                     ^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/core/model.py", line 274, in _solve
    casted_model = self.model(**solved_kw)
                   ^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/pydantic/main.py", line 171, in __init__
    self.__pydantic_validator__.validate_python(data, self_instance=self)
pydantic_core._pydantic_core.ValidationError: 1 validation error for update_feed
feed_id
  Input should be a valid integer [type=int_type, input_value={'item': {'id': 110, 'tit...e': None}, 'feed_id': 1}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.6/v/int_type
2024-03-20 13:11:21,413 INFO     - product_feeds | product_feeds.one_feed_update_requested | 35aed9db-d - Processed
2024-03-20 13:11:21,413 ERROR    - product_feeds | product_feeds.one_feed_update_requested | ac1e37a9-2 - ValidationError: 1 validation error for update_feed
feed_id
  Input should be a valid integer [type=int_type, input_value={'item': {'id': 107, 'tit...e': None}, 'feed_id': 1}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.6/v/int_type
Traceback (most recent call last):
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/handler.py", line 367, in consume
    raise e
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/handler.py", line 331, in consume
    result = await cast(
             ^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/utils.py", line 95, in set_message_wrapper
    return await func(message)
           ^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/nats/broker.py", line 244, in process_wrapper
    r = await func(message)
        ^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/core/asynchronous.py", line 406, in decode_wrapper
    return await func(msg)
           ^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/use.py", line 146, in injected_wrapper
    r = await real_model.asolve(
        ^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/core/model.py", line 519, in asolve
    final_args, final_kwargs, call = cast_gen.send(kwargs)
                                     ^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/core/model.py", line 274, in _solve
    casted_model = self.model(**solved_kw)
                   ^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/pydantic/main.py", line 171, in __init__
    self.__pydantic_validator__.validate_python(data, self_instance=self)
pydantic_core._pydantic_core.ValidationError: 1 validation error for update_feed
feed_id
  Input should be a valid integer [type=int_type, input_value={'item': {'id': 107, 'tit...e': None}, 'feed_id': 1}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.6/v/int_type
2024-03-20 13:11:21,414 INFO     - product_feeds | product_feeds.one_feed_update_requested | ac1e37a9-2 - Processed
2024-03-20 13:11:21,414 ERROR    - product_feeds | product_feeds.one_feed_update_requested | dfc4ee48-e - ValidationError: 1 validation error for update_feed
feed_id
  Input should be a valid integer [type=int_type, input_value={'item': {'id': 114, 'tit...e': None}, 'feed_id': 1}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.6/v/int_type
Traceback (most recent call last):
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/handler.py", line 367, in consume
    raise e
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/handler.py", line 331, in consume
    result = await cast(
             ^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/utils.py", line 95, in set_message_wrapper
    return await func(message)
           ^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/nats/broker.py", line 244, in process_wrapper
    r = await func(message)
        ^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/core/asynchronous.py", line 406, in decode_wrapper
    return await func(msg)
           ^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/use.py", line 146, in injected_wrapper
    r = await real_model.asolve(
        ^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/core/model.py", line 519, in asolve
    final_args, final_kwargs, call = cast_gen.send(kwargs)
                                     ^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/core/model.py", line 274, in _solve
    casted_model = self.model(**solved_kw)
                   ^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/pydantic/main.py", line 171, in __init__
    self.__pydantic_validator__.validate_python(data, self_instance=self)
pydantic_core._pydantic_core.ValidationError: 1 validation error for update_feed
feed_id
  Input should be a valid integer [type=int_type, input_value={'item': {'id': 114, 'tit...e': None}, 'feed_id': 1}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.6/v/int_type
2024-03-20 13:11:21,415 INFO     - product_feeds | product_feeds.one_feed_update_requested | dfc4ee48-e - Processed
2024-03-20 13:11:21,415 ERROR    - product_feeds | product_feeds.one_feed_update_requested | 5fdd1705-8 - ValidationError: 1 validation error for update_feed
feed_id
  Input should be a valid integer [type=int_type, input_value={'item': {'id': 108, 'tit...e': None}, 'feed_id': 1}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.6/v/int_type
Traceback (most recent call last):
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/handler.py", line 367, in consume
    raise e
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/handler.py", line 331, in consume
    result = await cast(
             ^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/utils.py", line 95, in set_message_wrapper
    return await func(message)
           ^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/nats/broker.py", line 244, in process_wrapper
    r = await func(message)
        ^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/core/asynchronous.py", line 406, in decode_wrapper
    return await func(msg)
           ^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/use.py", line 146, in injected_wrapper
    r = await real_model.asolve(
        ^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/core/model.py", line 519, in asolve
    final_args, final_kwargs, call = cast_gen.send(kwargs)
                                     ^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/core/model.py", line 274, in _solve
    casted_model = self.model(**solved_kw)
                   ^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/pydantic/main.py", line 171, in __init__
    self.__pydantic_validator__.validate_python(data, self_instance=self)
pydantic_core._pydantic_core.ValidationError: 1 validation error for update_feed
feed_id
  Input should be a valid integer [type=int_type, input_value={'item': {'id': 108, 'tit...e': None}, 'feed_id': 1}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.6/v/int_type
2024-03-20 13:11:21,416 INFO     - product_feeds | product_feeds.one_feed_update_requested | 5fdd1705-8 - Processed
2024-03-20 13:11:21,416 ERROR    - product_feeds | product_feeds.one_feed_update_requested | ba365302-f - ValidationError: 1 validation error for update_feed
feed_id
  Input should be a valid integer [type=int_type, input_value={'item': {'id': 115, 'tit...e': None}, 'feed_id': 1}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.6/v/int_type
Traceback (most recent call last):
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/handler.py", line 367, in consume
    raise e
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/handler.py", line 331, in consume
    result = await cast(
             ^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/utils.py", line 95, in set_message_wrapper
    return await func(message)
           ^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/nats/broker.py", line 244, in process_wrapper
    r = await func(message)
        ^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/core/asynchronous.py", line 406, in decode_wrapper
    return await func(msg)
           ^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/use.py", line 146, in injected_wrapper
    r = await real_model.asolve(
        ^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/core/model.py", line 519, in asolve
    final_args, final_kwargs, call = cast_gen.send(kwargs)
                                     ^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/core/model.py", line 274, in _solve
    casted_model = self.model(**solved_kw)
                   ^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/pydantic/main.py", line 171, in __init__
    self.__pydantic_validator__.validate_python(data, self_instance=self)
pydantic_core._pydantic_core.ValidationError: 1 validation error for update_feed
feed_id
  Input should be a valid integer [type=int_type, input_value={'item': {'id': 115, 'tit...e': None}, 'feed_id': 1}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.6/v/int_type
2024-03-20 13:11:21,423 INFO     - product_feeds | product_feeds.one_feed_update_requested | ba365302-f - Processed
2024-03-20 13:11:23,040 INFO     - product_feeds | product_feeds.feeds_update_requested    | 2893d5d3-8 - Received
2024-03-20 13:11:23,041 INFO     - product_feeds | product_feeds.feeds_update_requested    | 2d678717-7 - Received
2024-03-20 13:11:23,041 INFO     - product_feeds | product_feeds.feeds_update_requested    | afac684a-a - Received
2024-03-20 13:11:23,042 ERROR    - product_feeds | product_feeds.feeds_update_requested    | afac684a-a - ValidationError: 1 validation error for update_feeds
msg
  Input should be a valid string [type=string_type, input_value={'item': {'id': 5, 'title...e': None}, 'feed_id': 1}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.6/v/string_type
Traceback (most recent call last):
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/handler.py", line 367, in consume
    raise e
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/handler.py", line 331, in consume
    result = await cast(
             ^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/utils.py", line 95, in set_message_wrapper
    return await func(message)
           ^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/nats/broker.py", line 244, in process_wrapper
    r = await func(message)
        ^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/core/asynchronous.py", line 406, in decode_wrapper
    return await func(msg)
           ^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/use.py", line 146, in injected_wrapper
    r = await real_model.asolve(
        ^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/core/model.py", line 519, in asolve
    final_args, final_kwargs, call = cast_gen.send(kwargs)
                                     ^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/core/model.py", line 274, in _solve
    casted_model = self.model(**solved_kw)
                   ^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/pydantic/main.py", line 171, in __init__
    self.__pydantic_validator__.validate_python(data, self_instance=self)
pydantic_core._pydantic_core.ValidationError: 1 validation error for update_feeds
msg
  Input should be a valid string [type=string_type, input_value={'item': {'id': 5, 'title...e': None}, 'feed_id': 1}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.6/v/string_type
2024-03-20 13:11:23,045 INFO     - product_feeds | product_feeds.feeds_update_requested    | afac684a-a - Processed
2024-03-20 13:11:23,046 ERROR    - product_feeds | product_feeds.feeds_update_requested    | 2d678717-7 - ValidationError: 1 validation error for update_feeds
msg
  Input should be a valid string [type=string_type, input_value={'item': {'id': 4, 'title...e': None}, 'feed_id': 1}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.6/v/string_type
Traceback (most recent call last):
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/handler.py", line 367, in consume
    raise e
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/handler.py", line 331, in consume
    result = await cast(
             ^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/utils.py", line 95, in set_message_wrapper
    return await func(message)
           ^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/nats/broker.py", line 244, in process_wrapper
    r = await func(message)
        ^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/core/asynchronous.py", line 406, in decode_wrapper
    return await func(msg)
           ^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/use.py", line 146, in injected_wrapper
    r = await real_model.asolve(
        ^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/core/model.py", line 519, in asolve
    final_args, final_kwargs, call = cast_gen.send(kwargs)
                                     ^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/core/model.py", line 274, in _solve
    casted_model = self.model(**solved_kw)
                   ^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/pydantic/main.py", line 171, in __init__
    self.__pydantic_validator__.validate_python(data, self_instance=self)
pydantic_core._pydantic_core.ValidationError: 1 validation error for update_feeds
msg
  Input should be a valid string [type=string_type, input_value={'item': {'id': 4, 'title...e': None}, 'feed_id': 1}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.6/v/string_type
2024-03-20 13:11:23,049 INFO     - product_feeds | product_feeds.feeds_update_requested    | 2d678717-7 - Processed
2024-03-20 13:11:23,050 ERROR    - product_feeds | product_feeds.feeds_update_requested    | 2893d5d3-8 - ValidationError: 1 validation error for update_feeds
msg
  Input should be a valid string [type=string_type, input_value={'item': {'id': 3, 'title...e': None}, 'feed_id': 1}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.6/v/string_type
Traceback (most recent call last):
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/handler.py", line 367, in consume
    raise e
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/handler.py", line 331, in consume
    result = await cast(
             ^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/utils.py", line 95, in set_message_wrapper
    return await func(message)
           ^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/nats/broker.py", line 244, in process_wrapper
    r = await func(message)
        ^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/core/asynchronous.py", line 406, in decode_wrapper
    return await func(msg)
           ^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/use.py", line 146, in injected_wrapper
    r = await real_model.asolve(
        ^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/core/model.py", line 519, in asolve
    final_args, final_kwargs, call = cast_gen.send(kwargs)
                                     ^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/core/model.py", line 274, in _solve
    casted_model = self.model(**solved_kw)
                   ^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/pydantic/main.py", line 171, in __init__
    self.__pydantic_validator__.validate_python(data, self_instance=self)
pydantic_core._pydantic_core.ValidationError: 1 validation error for update_feeds
msg
  Input should be a valid string [type=string_type, input_value={'item': {'id': 3, 'title...e': None}, 'feed_id': 1}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.6/v/string_type
2024-03-20 13:11:23,052 INFO     - product_feeds | product_feeds.feeds_update_requested    | 2893d5d3-8 - Processed
2024-03-20 13:11:23,426 INFO     - product_feeds | product_feeds.one_feed_update_requested | 078d21d9-1 - Received
2024-03-20 13:11:23,426 INFO     - product_feeds | product_feeds.one_feed_update_requested | 9304e595-7 - Received
2024-03-20 13:11:23,427 INFO     - product_feeds | product_feeds.one_feed_update_requested | fde66322-2 - Received
2024-03-20 13:11:23,427 INFO     - product_feeds | product_feeds.one_feed_update_requested | b9f586c5-d - Received
2024-03-20 13:11:23,428 INFO     - product_feeds | product_feeds.one_feed_update_requested | 3098b75d-4 - Received
2024-03-20 13:11:23,428 INFO     - product_feeds | product_feeds.one_feed_update_requested | ec21f3f5-d - Received
2024-03-20 13:11:23,428 INFO     - product_feeds | product_feeds.one_feed_update_requested | 542fd010-9 - Received
2024-03-20 13:11:23,429 INFO     - product_feeds | product_feeds.one_feed_update_requested | 778823b2-5 - Received
2024-03-20 13:11:23,431 ERROR    - product_feeds | product_feeds.one_feed_update_requested | 078d21d9-1 - ValidationError: 1 validation error for update_feed
feed_id
  Input should be a valid integer [type=int_type, input_value={'item': {'id': 116, 'tit...e': None}, 'feed_id': 1}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.6/v/int_type
Traceback (most recent call last):
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/handler.py", line 367, in consume
    raise e
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/handler.py", line 331, in consume
    result = await cast(
             ^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/utils.py", line 95, in set_message_wrapper
    return await func(message)
           ^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/nats/broker.py", line 244, in process_wrapper
    r = await func(message)
        ^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/core/asynchronous.py", line 406, in decode_wrapper
    return await func(msg)
           ^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/use.py", line 146, in injected_wrapper
    r = await real_model.asolve(
        ^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/core/model.py", line 519, in asolve
    final_args, final_kwargs, call = cast_gen.send(kwargs)
                                     ^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/core/model.py", line 274, in _solve
    casted_model = self.model(**solved_kw)
                   ^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/pydantic/main.py", line 171, in __init__
    self.__pydantic_validator__.validate_python(data, self_instance=self)
pydantic_core._pydantic_core.ValidationError: 1 validation error for update_feed
feed_id
  Input should be a valid integer [type=int_type, input_value={'item': {'id': 116, 'tit...e': None}, 'feed_id': 1}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.6/v/int_type
2024-03-20 13:11:23,434 INFO     - product_feeds | product_feeds.one_feed_update_requested | 078d21d9-1 - Processed
2024-03-20 13:11:23,435 ERROR    - product_feeds | product_feeds.one_feed_update_requested | 542fd010-9 - ValidationError: 1 validation error for update_feed
feed_id
  Input should be a valid integer [type=int_type, input_value={'item': {'id': 122, 'tit...e': None}, 'feed_id': 1}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.6/v/int_type
Traceback (most recent call last):
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/handler.py", line 367, in consume
    raise e
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/handler.py", line 331, in consume
    result = await cast(
             ^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/utils.py", line 95, in set_message_wrapper
    return await func(message)
           ^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/nats/broker.py", line 244, in process_wrapper
    r = await func(message)
        ^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/core/asynchronous.py", line 406, in decode_wrapper
    return await func(msg)
           ^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/use.py", line 146, in injected_wrapper
    r = await real_model.asolve(
        ^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/core/model.py", line 519, in asolve
    final_args, final_kwargs, call = cast_gen.send(kwargs)
                                     ^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/core/model.py", line 274, in _solve
    casted_model = self.model(**solved_kw)
                   ^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/pydantic/main.py", line 171, in __init__
    self.__pydantic_validator__.validate_python(data, self_instance=self)
pydantic_core._pydantic_core.ValidationError: 1 validation error for update_feed
feed_id
  Input should be a valid integer [type=int_type, input_value={'item': {'id': 122, 'tit...e': None}, 'feed_id': 1}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.6/v/int_type
2024-03-20 13:11:23,436 INFO     - product_feeds | product_feeds.one_feed_update_requested | 542fd010-9 - Processed
2024-03-20 13:11:23,437 ERROR    - product_feeds | product_feeds.one_feed_update_requested | fde66322-2 - ValidationError: 1 validation error for update_feed
feed_id
  Input should be a valid integer [type=int_type, input_value={'item': {'id': 118, 'tit...e': None}, 'feed_id': 1}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.6/v/int_type
Traceback (most recent call last):
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/handler.py", line 367, in consume
    raise e
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/handler.py", line 331, in consume
    result = await cast(
             ^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/utils.py", line 95, in set_message_wrapper
    return await func(message)
           ^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/nats/broker.py", line 244, in process_wrapper
    r = await func(message)
        ^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/core/asynchronous.py", line 406, in decode_wrapper
    return await func(msg)
           ^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/use.py", line 146, in injected_wrapper
    r = await real_model.asolve(
        ^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/core/model.py", line 519, in asolve
    final_args, final_kwargs, call = cast_gen.send(kwargs)
                                     ^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/core/model.py", line 274, in _solve
    casted_model = self.model(**solved_kw)
                   ^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/pydantic/main.py", line 171, in __init__
    self.__pydantic_validator__.validate_python(data, self_instance=self)
pydantic_core._pydantic_core.ValidationError: 1 validation error for update_feed
feed_id
  Input should be a valid integer [type=int_type, input_value={'item': {'id': 118, 'tit...e': None}, 'feed_id': 1}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.6/v/int_type
2024-03-20 13:11:23,439 INFO     - product_feeds | product_feeds.one_feed_update_requested | fde66322-2 - Processed
2024-03-20 13:11:23,440 ERROR    - product_feeds | product_feeds.one_feed_update_requested | b9f586c5-d - ValidationError: 1 validation error for update_feed
feed_id
  Input should be a valid integer [type=int_type, input_value={'item': {'id': 119, 'tit...e': None}, 'feed_id': 1}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.6/v/int_type
Traceback (most recent call last):
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/handler.py", line 367, in consume
    raise e
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/handler.py", line 331, in consume
    result = await cast(
             ^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/utils.py", line 95, in set_message_wrapper
    return await func(message)
           ^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/nats/broker.py", line 244, in process_wrapper
    r = await func(message)
        ^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/core/asynchronous.py", line 406, in decode_wrapper
    return await func(msg)
           ^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/use.py", line 146, in injected_wrapper
    r = await real_model.asolve(
        ^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/core/model.py", line 519, in asolve
    final_args, final_kwargs, call = cast_gen.send(kwargs)
                                     ^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/core/model.py", line 274, in _solve
    casted_model = self.model(**solved_kw)
                   ^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/pydantic/main.py", line 171, in __init__
    self.__pydantic_validator__.validate_python(data, self_instance=self)
pydantic_core._pydantic_core.ValidationError: 1 validation error for update_feed
feed_id
  Input should be a valid integer [type=int_type, input_value={'item': {'id': 119, 'tit...e': None}, 'feed_id': 1}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.6/v/int_type
2024-03-20 13:11:23,441 INFO     - product_feeds | product_feeds.one_feed_update_requested | b9f586c5-d - Processed
2024-03-20 13:11:23,442 ERROR    - product_feeds | product_feeds.one_feed_update_requested | ec21f3f5-d - ValidationError: 1 validation error for update_feed
feed_id
  Input should be a valid integer [type=int_type, input_value={'item': {'id': 121, 'tit...e': None}, 'feed_id': 1}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.6/v/int_type
Traceback (most recent call last):
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/handler.py", line 367, in consume
    raise e
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/handler.py", line 331, in consume
    result = await cast(
             ^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/utils.py", line 95, in set_message_wrapper
    return await func(message)
           ^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/nats/broker.py", line 244, in process_wrapper
    r = await func(message)
        ^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/core/asynchronous.py", line 406, in decode_wrapper
    return await func(msg)
           ^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/use.py", line 146, in injected_wrapper
    r = await real_model.asolve(
        ^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/core/model.py", line 519, in asolve
    final_args, final_kwargs, call = cast_gen.send(kwargs)
                                     ^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/core/model.py", line 274, in _solve
    casted_model = self.model(**solved_kw)
                   ^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/pydantic/main.py", line 171, in __init__
    self.__pydantic_validator__.validate_python(data, self_instance=self)
pydantic_core._pydantic_core.ValidationError: 1 validation error for update_feed
feed_id
  Input should be a valid integer [type=int_type, input_value={'item': {'id': 121, 'tit...e': None}, 'feed_id': 1}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.6/v/int_type
2024-03-20 13:11:23,443 INFO     - product_feeds | product_feeds.one_feed_update_requested | ec21f3f5-d - Processed
2024-03-20 13:11:23,443 ERROR    - product_feeds | product_feeds.one_feed_update_requested | 3098b75d-4 - ValidationError: 1 validation error for update_feed
feed_id
  Input should be a valid integer [type=int_type, input_value={'item': {'id': 120, 'tit...e': None}, 'feed_id': 1}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.6/v/int_type
Traceback (most recent call last):
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/handler.py", line 367, in consume
    raise e
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/handler.py", line 331, in consume
    result = await cast(
             ^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/utils.py", line 95, in set_message_wrapper
    return await func(message)
           ^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/nats/broker.py", line 244, in process_wrapper
    r = await func(message)
        ^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/core/asynchronous.py", line 406, in decode_wrapper
    return await func(msg)
           ^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/use.py", line 146, in injected_wrapper
    r = await real_model.asolve(
        ^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/core/model.py", line 519, in asolve
    final_args, final_kwargs, call = cast_gen.send(kwargs)
                                     ^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/core/model.py", line 274, in _solve
    casted_model = self.model(**solved_kw)
                   ^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/pydantic/main.py", line 171, in __init__
    self.__pydantic_validator__.validate_python(data, self_instance=self)
pydantic_core._pydantic_core.ValidationError: 1 validation error for update_feed
feed_id
  Input should be a valid integer [type=int_type, input_value={'item': {'id': 120, 'tit...e': None}, 'feed_id': 1}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.6/v/int_type
2024-03-20 13:11:23,445 INFO     - product_feeds | product_feeds.one_feed_update_requested | 3098b75d-4 - Processed
2024-03-20 13:11:23,445 ERROR    - product_feeds | product_feeds.one_feed_update_requested | 9304e595-7 - ValidationError: 1 validation error for update_feed
feed_id
  Input should be a valid integer [type=int_type, input_value={'item': {'id': 117, 'tit...e': None}, 'feed_id': 1}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.6/v/int_type
Traceback (most recent call last):
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/handler.py", line 367, in consume
    raise e
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/handler.py", line 331, in consume
    result = await cast(
             ^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/utils.py", line 95, in set_message_wrapper
    return await func(message)
           ^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/nats/broker.py", line 244, in process_wrapper
    r = await func(message)
        ^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/core/asynchronous.py", line 406, in decode_wrapper
    return await func(msg)
           ^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/use.py", line 146, in injected_wrapper
    r = await real_model.asolve(
        ^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/core/model.py", line 519, in asolve
    final_args, final_kwargs, call = cast_gen.send(kwargs)
                                     ^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/core/model.py", line 274, in _solve
    casted_model = self.model(**solved_kw)
                   ^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/pydantic/main.py", line 171, in __init__
    self.__pydantic_validator__.validate_python(data, self_instance=self)
pydantic_core._pydantic_core.ValidationError: 1 validation error for update_feed
feed_id
  Input should be a valid integer [type=int_type, input_value={'item': {'id': 117, 'tit...e': None}, 'feed_id': 1}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.6/v/int_type
2024-03-20 13:11:23,447 INFO     - product_feeds | product_feeds.one_feed_update_requested | 9304e595-7 - Processed
2024-03-20 13:11:23,447 ERROR    - product_feeds | product_feeds.one_feed_update_requested | 778823b2-5 - ValidationError: 1 validation error for update_feed
feed_id
  Input should be a valid integer [type=int_type, input_value={'item': {'id': 123, 'tit...e': None}, 'feed_id': 1}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.6/v/int_type
Traceback (most recent call last):
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/handler.py", line 367, in consume
    raise e
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/handler.py", line 331, in consume
    result = await cast(
             ^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/utils.py", line 95, in set_message_wrapper
    return await func(message)
           ^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/nats/broker.py", line 244, in process_wrapper
    r = await func(message)
        ^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/faststream/broker/core/asynchronous.py", line 406, in decode_wrapper
    return await func(msg)
           ^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/use.py", line 146, in injected_wrapper
    r = await real_model.asolve(
        ^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/core/model.py", line 519, in asolve
    final_args, final_kwargs, call = cast_gen.send(kwargs)
                                     ^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/fast_depends/core/model.py", line 274, in _solve
    casted_model = self.model(**solved_kw)
                   ^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/Silver/Projects/sandbox/faststream-issue/.venv/lib/python3.12/site-packages/pydantic/main.py", line 171, in __init__
    self.__pydantic_validator__.validate_python(data, self_instance=self)
pydantic_core._pydantic_core.ValidationError: 1 validation error for update_feed
feed_id
  Input should be a valid integer [type=int_type, input_value={'item': {'id': 123, 'tit...e': None}, 'feed_id': 1}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.6/v/int_type
2024-03-20 13:11:23,449 INFO     - product_feeds | product_feeds.one_feed_update_requested | 778823b2-5 - Processed
^C2024-03-20 13:13:33,878 INFO     - FastStream app shutting down...
2024-03-20 13:13:33,881 INFO     - FastStream app shut down gracefully.

faststream-issue master*​​ 2m27s 
```
`
