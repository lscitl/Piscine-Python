# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Makefile                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: seseo <seseo@student.42.fr>                +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/06/02 17:22:13 by seseo             #+#    #+#              #
#    Updated: 2023/06/14 19:46:48 by seseo            ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

TARGET				:= PiscinePython
IMG					:= python3
PWD					:= `$(shell pwd)`

.PHONY:	all
all:	run

.PHONY: build
build:	
		docker build -t $(IMG) ./

.PHONY:	run
run:	build
		@docker run \
		--rm -it \
		--name $(TARGET) \
		--mount type=bind,source=`$(PWD)`,target=/app \
		--workdir /app \
		$(IMG)

.PHONY:	re
re:		
		make run

.PHONY:	clean
clean:	
		
		
.PHONY:	fclean
fclean: clean
		docker image rm $(IMG)