# Django & Pact image upload error

## Replication steps
1. Run `docker-compose build repro && docker-compose run repro`

### Expected outcome:
The pact log `pact-mock-service.log` should show one unexpected request
that didn't match anything but NO errors.

### Actual result:

Pact encounters this error:
```
E, [2018-12-04T09:01:40.958484 #9] ERROR -- : Error ocurred in mock service: Encoding::UndefinedConversionError - "\xFF" from ASCII-8BIT to UTF-8
E, [2018-12-04T09:01:40.959014 #9] ERROR -- : /usr/local/lib/python2.7/site-packages/pact/bin/pact/lib/vendor/ruby/2.2.0/gems/pact-mock_service-2.10.1/lib/pact/mock_service/request_handlers/interaction_replay.rb:16:in `encode'
/usr/local/lib/python2.7/site-packages/pact/bin/pact/lib/vendor/ruby/2.2.0/gems/pact-mock_service-2.10.1/lib/pact/mock_service/request_handlers/interaction_replay.rb:16:in `to_json'
/usr/local/lib/python2.7/site-packages/pact/bin/pact/lib/vendor/ruby/2.2.0/gems/pact-mock_service-2.10.1/lib/pact/mock_service/request_handlers/interaction_replay.rb:16:in `pretty_generate'
/usr/local/lib/python2.7/site-packages/pact/bin/pact/lib/vendor/ruby/2.2.0/gems/pact-mock_service-2.10.1/lib/pact/mock_service/request_handlers/interaction_replay.rb:49:in `find_response'
/usr/local/lib/python2.7/site-packages/pact/bin/pact/lib/vendor/ruby/2.2.0/gems/pact-mock_service-2.10.1/lib/pact/mock_service/request_handlers/interaction_replay.rb:41:in `respond'
/usr/local/lib/python2.7/site-packages/pact/bin/pact/lib/vendor/ruby/2.2.0/gems/pact-mock_service-2.10.1/lib/pact/mock_service/request_handlers/base_request_handler.rb:17:in `call'
/usr/local/lib/python2.7/site-packages/pact/bin/pact/lib/vendor/ruby/2.2.0/gems/rack-2.0.5/lib/rack/cascade.rb:33:in `block in call'
/usr/local/lib/python2.7/site-packages/pact/bin/pact/lib/vendor/ruby/2.2.0/gems/rack-2.0.5/lib/rack/cascade.rb:24:in `each'
/usr/local/lib/python2.7/site-packages/pact/bin/pact/lib/vendor/ruby/2.2.0/gems/rack-2.0.5/lib/rack/cascade.rb:24:in `call'
/usr/local/lib/python2.7/site-packages/pact/bin/pact/lib/vendor/ruby/2.2.0/gems/pact-mock_service-2.10.1/lib/pact/consumer/mock_service/cors_origin_header_middleware.rb:11:in `call'
/usr/local/lib/python2.7/site-packages/pact/bin/pact/lib/vendor/ruby/2.2.0/gems/pact-mock_service-2.10.1/lib/pact/consumer/mock_service/error_handler.rb:13:in `call'
/usr/local/lib/python2.7/site-packages/pact/bin/pact/lib/vendor/ruby/2.2.0/gems/pact-mock_service-2.10.1/lib/pact/mock_service/app.rb:33:in `call'
/usr/local/lib/python2.7/site-packages/pact/bin/pact/lib/vendor/ruby/2.2.0/gems/pact-mock_service-2.10.1/lib/pact/consumer/mock_service/set_location.rb:14:in `call'
/usr/local/lib/python2.7/site-packages/pact/bin/pact/lib/vendor/ruby/2.2.0/gems/rack-2.0.5/lib/rack/handler/webrick.rb:86:in `service'
/usr/local/lib/python2.7/site-packages/pact/bin/pact/lib/vendor/ruby/2.2.0/gems/webrick-1.3.1/lib/webrick/httpserver.rb:138:in `service'
/usr/local/lib/python2.7/site-packages/pact/bin/pact/lib/vendor/ruby/2.2.0/gems/webrick-1.3.1/lib/webrick/httpserver.rb:94:in `run'
/usr/local/lib/python2.7/site-packages/pact/bin/pact/lib/vendor/ruby/2.2.0/gems/webrick-1.3.1/lib/webrick/server.rb:191:in `block in start_thread'
```