# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Makefile                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: seseo <seseo@student.42.fr>                +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/06/02 17:22:13 by seseo             #+#    #+#              #
#    Updated: 2023/06/12 23:36:39 by seseo            ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

TARGET				:= PiscinePython

.PHONY:	all
all:	run

.PHONY:	run
run:
		docker run \
		--rm -it --entrypoint bash \
		--name $(TARGET) \
		--mount type=bind,source=$(HOME)/Piscine-Python/Python-0-Starting,target=/app,readonly \
		--workdir /app \
		python:3.10

.PHONY:	stop
stop:
		docker container stop $(TARGET)

.PHONY:	re
re:		clean
		make run

.PHONY:	clean
clean:	stop

.PHONY:	fclean
fclean: clean
		