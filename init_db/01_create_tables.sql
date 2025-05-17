DROP TABLE IF EXISTS results, fragments, users CASCADE;

CREATE TABLE users (
  user_id SERIAL PRIMARY KEY,
  full_name VARCHAR(255) NOT NULL,
  email VARCHAR(255) UNIQUE NOT NULL,
  program VARCHAR(100) NOT NULL CHECK (program IN ('basic', 'advanced', 'pro')),
  password_hash VARCHAR(255) NOT NULL,
  created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE fragments (
  fragment_id SERIAL PRIMARY KEY,
  content TEXT NOT NULL,
  complexity_level VARCHAR(50) NOT NULL CHECK (complexity_level IN ('beginner', 'intermediate', 'expert')),
  theme VARCHAR(100) NOT NULL,
  author VARCHAR(100),
  added_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
  metadata JSONB
);

CREATE TABLE results (
  result_id SERIAL PRIMARY KEY,
  user_id INT NOT NULL REFERENCES users(user_id) ON DELETE CASCADE,
  fragment_id INT NOT NULL REFERENCES fragments(fragment_id) ON DELETE CASCADE,
  test_date TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
  reading_speed INT NOT NULL CHECK (reading_speed > 0),
  comprehension DECIMAL(5,2) CHECK (comprehension BETWEEN 0 AND 100),
  session_data JSONB NOT NULL
);

CREATE INDEX idx_results_user_date ON results(user_id, test_date);
CREATE INDEX idx_fragments_complexity ON fragments(complexity_level);
CREATE INDEX idx_users_program ON users(program);
