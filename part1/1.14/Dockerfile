FROM ruby:2.6.0
WORKDIR /home 
RUN apt-get update && apt-get install -y git
RUN apt-get update && apt-get install -y curl
RUN curl -sL https://deb.nodesource.com/setup_10.x | bash
RUN apt-get install -y nodejs
RUN git clone https://github.com/docker-hy/rails-example-project .
RUN gem install bundler
RUN bundle install
RUN rails db:migrate
EXPOSE 3000
CMD rails s
