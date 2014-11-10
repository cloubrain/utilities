# -*- coding: utf-8 -*-
from gevent.queue import Empty, Full, Queue
from gevent import Greenlet, sleep

# This file is part of Utilities.
#
#     Utilities is free software: you can redistribute it and/or modify
#     it under the terms of the GNU Lesser General Public License as published by
#     the Free Software Foundation, either version 3 of the License, or
#     (at your option) any later version.
#
#     Utilities is distributed in the hope that it will be useful,
#     but WITHOUT ANY WARRANTY; without even the implied warranty of
#     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#     GNU Lesser General Public License for more details.
#
#     You should have received a copy of the GNU Lesser General Public License
#     along with Utilities.  If not, see <http://www.gnu.org/licenses/>.

__author__ = 'horia margarit'


class Consumer(Greenlet):

    def __init__(self, *args, **kwargs):
        args = list(args)
        self.__producers = 0
        self.__queue = args.pop(1)
        self.__process = args.pop(0)
        self.__rest = kwargs.pop('rest', 20)
        super(Consumer, self).__init__(*args, **kwargs)

    def _run(self):
        empty_queue = False if self.__queue.qsize() else True
        while not empty_queue or self.__producers:
            try:
                element = self.__queue.get_nowait()
            except Empty as e:
                sleep(self.__rest)
            else:
                self.__process(element)
            empty_queue = False if self.__queue.qsize() else True

    def register_producer(self):
        self.__producers += 1

    def remove_producer(self):
        self.__producers -= 1


class Producer(Greenlet):

    def __init__(self, *args, **kwargs):
        args = list(args)
        self.__terminate = False
        self.__consumers = args.pop(2)
        self.__queue = args.pop(1)
        self.__delegator = args.pop(0)
        self.__rest = kwargs.pop('rest', 20)
        super(Producer, self).__init__(*args, **kwargs)

    def _run(self):
        try:
            element = self.__delegator.next()
        except StopIteration as e:
            self.__terminate = True
        [consumer.register_producer() for consumer in self.__consumers]
        while not self.__terminate:
            try:
                self.__queue.put_nowait(element)
            except Full as e:
                sleep(self.__rest)
            else:
                try:
                    element = self.__delegator.next()
                except StopIteration as e:
                    self.__terminate = True

    def stop(self):
        [consumer.remove_producer() for consumer in self.__consumers]
        self.__terminate = True


if __name__ == '__main__':

    def dummy_manager():
        job = 1L
        while True:
            yield job
            job += 1L

    def dummy_worker(job):
        print("%s\n%r\n" % (job, job, ))

    work = Queue(maxsize=2048)
    c = Consumer(dummy_worker, work, rest=3)
    p = Producer(dummy_manager(), work, [c], rest=3)
    p.start()
    c.start()

    sleep(12)
    p.stop()
    p.join()
    c.join()
    print("Completed!")

