#!/bin/bash


set -eu


# check/set variables
vid=${1:?$'\r\e[K'hexadecimal (ex. 02ad) vendor ID is required (vid [pid] [usb.ids])}
[[ "${vid,,}" =~ ^[0-9a-f]{4}$ ]] ||
	vid=${error:?$'\r\e[K'bad hexadecimal (ex. 02ad) vendor ID}

pid=${2:-}
[ "${pid}" ] &&
	! [[ "${pid,,}" =~ ^([0-9a-f]{4})|-$ ]] &&
		pid=${error:?$'\r\e[K'bad hexadecimal (ex. 138c) product ID}

hwdata=${3:-/usr/share/hwdata/usb.ids}

[ "${4:-}" ] && error=${error:?$'\r\e[K'too many arguments}


# extract vendor ID section from hwdata file
vidpids=$( sed -n "/^${vid} /I,/^[^\t]/{x;/^$/!p}" "$hwdata" )


# translate vid and pid
if [ "${vidpids}" ]
then

	# get vid and remove extra spaces
	_vid=$( head -1 <<< "${vidpids}" )
	_vid=$( echo ${_vid:4} )
	vid="${_vid} (${vid,,})"

	# get pid and remove extra spaces
	_pid=$( grep -i -m 1 ^$'\t'"${pid} " <<< "${vidpids}" || true )
	_pid=$( echo ${_pid:5} )
	[ "${_pid}" ] && pid="${_pid} (${pid,,})"

	echo ${vid}"$( [ "${_pid}" ] && echo $'\t'${pid} )"

fi
