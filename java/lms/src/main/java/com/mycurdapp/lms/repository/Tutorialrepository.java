package com.mycurdapp.lms.repository;

import java.util.List;
import com.mycurdapp.lms.model.Tutorial;
import org.springframework.data.jpa.repository.JpaRepository;
// import com.example.crud_restapi.model.Tutorial;

public interface Tutorialrepository extends JpaRepository<Tutorial, Long> {
  List<Tutorial> findByPublished(boolean published);
  List<Tutorial> findByTitleContainingIgnoreCase(String title);
}
