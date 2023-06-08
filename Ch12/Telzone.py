##전화번호 지역번호 검색
zoneno = ([['010'], '휴대전화'],
          ['02', ['서울특별시', '광명시', '과천시']], ['031', '경기도'], ['032', ['인천광역시', '부천시']], ['033', '강원도'],
          ['041', '충청남도'], ['042', ['대전광역시', '계룡시']], ['043', '충청북도'], ['044', '세종특별자치시'],
          ['051', '부산광역시'], ['052', '울산광역시'], ['053', ['대구광역시', '경산시']], ['054', '경상북도'],
          ['055', '경상남도'], ['061', '전라남도'], ['062', '광주광역시'], ['063', '전라북도'], ['064', '제주특별자치도'])

def get_zone(inno):  #지역번호로 검색
    for no, zone in zoneno:
        if type(no) is list:  # 항목 형식이 리스트인지 확인
            if inno in no:  # 리스트 항목에서 찾기
                return zone
            elif no == inno:  # 일반 항목일 경우 일치 비교
                return zone
        else:
            if no == inno:
                return zone

def get_no(inzone):
    for no, zone in zoneno:
        if type(zone) is list:  # 항목 형식이 리스트인지 확인
            for zlist in zone:
                if inzone in zlist:
                    return no
        elif zone.find(inzone) >= 0:  # 일반 항목일 경우 일치 비교
            return no