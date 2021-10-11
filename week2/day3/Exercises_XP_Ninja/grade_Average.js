function findAvg(gradesList) {
    let marks = prompt("Enter your notes to calculate your average separate by comma")
    marks.split(',')
    let Student = []
    for(let i=0;i<marks;i++) {
        Student.push(marks[i])
    }
    let sumMarks=0
    for(let i=0;i<Student.length;i++) {
    sumMarks=sumMarks+Student[i]
    }
    let totalMarksNumber = Student.length
    let average = sumMarks/totalMarksNumber

    if(average<65) {
        alert("You failed")
    } else {
        alert("You passed")
    }
}