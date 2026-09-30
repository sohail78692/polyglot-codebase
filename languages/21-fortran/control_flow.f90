! ==========================================
! Program: Control Flow in Fortran
! ==========================================

program control_flow
    implicit none
    integer :: num, i, count
    character(len=1) :: grade

    ! 1. Conditionals
    print *, "Conditionals:"
    num = 15
    if (num > 0) then
        if (mod(num, 2) == 0) then
            print '(I0, A)', num, " is Positive and Even"
        else
            print '(I0, A)', num, " is Positive and Odd"
        end if
    else if (num < 0) then
        print '(I0, A)', num, " is Negative"
    else
        print *, "Number is Zero"
    end if

    print *, ""
    print *, "Pattern Matching / Switch:"
    ! 2. Select Case
    grade = 'B'
    select case (grade)
        case ('A')
            print *, "Grade A: Excellent!"
        case ('B')
            print *, "Grade B: Good Job!"
        case ('C')
            print *, "Grade C: Fair"
        case default
            print *, "Keep Trying!"
    end select

    print *, ""
    print *, "For Loop (1 to 5):"
    ! 3. Do Loop (For Loop equivalent)
    do i = 1, 5
        if (i == 5) then
            write(*, '(I0)') i
        else
            write(*, '(I0, 1X)', advance='no') i
        end if
    end do

    print *, ""
    print *, "While Loop (Countdown):"
    ! 4. Do While Loop
    count = 3
    do while (count > 0)
        write(*, '(I0, 1X)', advance='no') count
        count = count - 1
    end do
    print *, "Blastoff!"

end program control_flow
